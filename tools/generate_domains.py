"""Generate one Python module for every domain in a CDP descriptor."""

from __future__ import annotations

import argparse
import json
import keyword
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import TypeAlias, cast

JsonValue: TypeAlias = (
    bool | int | float | str | list["JsonValue"] | dict[str, "JsonValue"] | None
)
JsonObject: TypeAlias = dict[str, JsonValue]

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PROTOCOL = ROOT / "chrome-remote-interface" / "lib" / "protocol.json"
DEFAULT_PACKAGE = ROOT / "cdp"


def snake_case(name: str) -> str:
    """Convert a CDP domain name into a readable module name."""

    first = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", name)
    return re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", first).lower()


def title_name(name: str) -> str:
    return name[:1].upper() + name[1:]


def normalize_json(value: object) -> JsonValue:
    """Convert ``json.loads`` output into a fully bounded recursive type."""

    if value is None or isinstance(value, bool | int | float | str):
        return value
    if isinstance(value, list):
        return [normalize_json(item) for item in cast(list[object], value)]
    if isinstance(value, dict):
        result: JsonObject = {}
        for key, item in cast(dict[object, object], value).items():
            if not isinstance(key, str):
                raise ValueError("JSON object key is not a string")
            result[key] = normalize_json(item)
        return result
    raise ValueError(f"Unsupported JSON value: {type(value).__name__}")


def load_json_object(path: Path) -> JsonObject:
    raw: object = json.loads(path.read_text(encoding="utf-8"))
    value = normalize_json(raw)
    if not isinstance(value, dict):
        raise ValueError(f"{path} does not contain a JSON object")
    return value


def object_list(item: JsonObject, key: str) -> list[JsonObject]:
    value = item.get(key)
    if not isinstance(value, list):
        return []
    return [child for child in value if isinstance(child, dict)]


def description(item: JsonObject, fallback: str) -> str:
    value = str(item.get("description", fallback))
    return " ".join(value.split()).replace('"""', r"\"\"\"")


def annotation(schema: JsonObject, current_domain: str) -> str:
    reference = schema.get("$ref")
    if isinstance(reference, str):
        if "." in reference:
            domain, type_name = reference.split(".", 1)
            if domain != current_domain:
                return f"{domain}.{type_name}"
            return type_name
        return reference
    kind = schema.get("type")
    if kind == "string":
        values = schema.get("enum")
        if isinstance(values, list) and values:
            literals = ", ".join(repr(value) for value in values)
            return f"Literal[{literals}]"
        return "str"
    if kind == "integer":
        return "int"
    if kind == "number":
        return "float"
    if kind == "boolean":
        return "bool"
    if kind == "array":
        items = schema.get("items")
        item_type = (
            annotation(items, current_domain)
            if isinstance(items, dict)
            else "JsonValue"
        )
        return f"list[{item_type}]"
    if kind == "object":
        return "JsonObject"
    return "JsonValue"


def typed_dict(
    name: str,
    fields: list[JsonObject],
    current_domain: str,
) -> list[str]:
    entries: list[str] = []
    for field in fields:
        field_name = str(field["name"])
        if not field_name.isidentifier() or keyword.iskeyword(field_name):
            raise ValueError(f"{name}.{field_name} is not a Python identifier")
        field_type = annotation(field, current_domain)
        if field.get("optional"):
            field_type = f"NotRequired[{field_type}]"
        entries.append(f"    {field_name}: {field_type}")
    if not entries:
        return [f"{name}: TypeAlias = JsonObject", ""]
    return [f"class {name}(TypedDict):", *entries, ""]


def referenced_domains(domain: JsonObject) -> list[str]:
    references: set[str] = set()

    def visit(value: JsonValue) -> None:
        if isinstance(value, dict):
            reference = value.get("$ref")
            if isinstance(reference, str) and "." in reference:
                references.add(reference.split(".", 1)[0])
            for child in value.values():
                visit(child)
        elif isinstance(value, list):
            for child in value:
                visit(child)

    visit(domain)
    references.discard(str(domain["domain"]))
    return sorted(references)


def generate_domain(domain: JsonObject) -> str:
    domain_name = str(domain["domain"])
    references = referenced_domains(domain)
    types = object_list(domain, "types")
    commands = object_list(domain, "commands")
    events = object_list(domain, "events")
    schema_items = [*types, *commands, *events]
    has_alias = any(not isinstance(item.get("properties"), list) for item in types)
    has_literal = any(
        isinstance(value.get("enum"), list)
        for item in schema_items
        for value in _walk_dicts(item)
    )
    fields = [
        field
        for item in schema_items
        for key in ("properties", "parameters", "returns")
        for field in object_list(item, key)
    ]
    has_typed_dict = bool(fields)
    typing_names = [
        name
        for name, needed in (
            ("TYPE_CHECKING", bool(references)),
            ("Literal", has_literal),
            ("TypeAlias", has_alias),
            (
                "cast",
                bool(events)
                or any(object_list(command, "returns") for command in commands),
            ),
            (
                "overload",
                bool(
                    events
                    or any(object_list(command, "parameters") for command in commands)
                ),
            ),
        )
        if needed
    ]
    extension_names = [
        name
        for name, needed in (
            ("NotRequired", any(field.get("optional") for field in fields)),
            ("TypedDict", has_typed_dict),
            ("Unpack", any(object_list(command, "parameters") for command in commands)),
        )
        if needed
    ]
    collection_names = ["Mapping"]
    if events:
        collection_names.insert(0, "Awaitable")
    domain_names = ["Domain as BaseDomain"]
    if events:
        domain_names.extend(["EventCallback", "Unsubscribe"])
    lines = [
        '"""Generated bindings for the CDP '
        + domain_name
        + ' domain. Do not edit manually."""',
        "",
        "from __future__ import annotations",
        "",
        f"from collections.abc import {', '.join(collection_names)}",
    ]
    if typing_names:
        lines.append(f"from typing import {', '.join(typing_names)}")
    if extension_names:
        lines.extend(
            [
                "",
                f"from typing_extensions import {', '.join(extension_names)}",
            ]
        )
    lines.extend(
        [
            "",
            f"from cdp.domain import {', '.join(domain_names)}",
            "from cdp.types import JsonObject, JsonValue",
        ]
    )
    if references:
        lines.extend(["", "if TYPE_CHECKING:"])
        for reference in references:
            lines.append(f"    from . import {snake_case(reference)} as {reference}")
    lines.extend(["", ""])

    type_names = {str(item["id"]) for item in types}
    class_name = f"{domain_name}Domain" if domain_name in type_names else domain_name
    exported: list[str] = [class_name]
    for raw_type in types:
        type_name = str(raw_type["id"])
        exported.append(type_name)
        properties = object_list(raw_type, "properties")
        if properties:
            lines.extend(typed_dict(type_name, properties, domain_name))
        else:
            alias = annotation(raw_type, domain_name)
            if "." in alias:
                alias = repr(alias)
            lines.extend(
                [
                    f"{type_name}: TypeAlias = {alias}",
                    "",
                ]
            )

    for command in commands:
        base_name = title_name(str(command["name"]))
        parameters = object_list(command, "parameters")
        returns = object_list(command, "returns")
        if parameters:
            name = f"{base_name}Parameters"
            exported.append(name)
            lines.extend(typed_dict(name, parameters, domain_name))
        if returns:
            name = f"{base_name}Result"
            exported.append(name)
            lines.extend(typed_dict(name, returns, domain_name))

    for event in events:
        parameters = object_list(event, "parameters")
        if parameters:
            name = f"{title_name(str(event['name']))}Event"
            exported.append(name)
            lines.extend(typed_dict(name, parameters, domain_name))

    lines.extend(
        [
            f"class {class_name}(BaseDomain):",
            f'    """{description(domain, f"The CDP {domain_name} domain.")}"""',
            "",
            f'    domain_name = "{domain_name}"',
        ]
    )
    if not commands and not events:
        lines.extend(["", "    pass"])

    for command in commands:
        command_name = str(command["name"])
        base_name = title_name(command_name)
        parameters = object_list(command, "parameters")
        returns = object_list(command, "returns")
        result_type = f"{base_name}Result" if returns else "JsonObject"
        lines.append("")
        if parameters:
            params_type = f"{base_name}Parameters"
            lines.extend(
                [
                    "    @overload",
                    f"    async def {command_name}(",
                    "        self,",
                    f"        params: {params_type},",
                    "        session_id: str | None = None,",
                    f"    ) -> {result_type}: ...",
                    "",
                    "    @overload",
                    f"    async def {command_name}(",
                    "        self,",
                    "        params: str | None = None,",
                    "        session_id: str | None = None,",
                    f"        **kwargs: Unpack[{params_type}],",
                    f"    ) -> {result_type}: ...",
                    "",
                    f"    async def {command_name}(",
                    "        self,",
                    "        params: Mapping[str, object] | str | None = None,",
                    "        session_id: str | None = None,",
                    "        **kwargs: object,",
                    f"    ) -> {result_type}:",
                ]
            )
        else:
            lines.extend(
                [
                    f"    async def {command_name}(",
                    "        self,",
                    "        session_id: str | None = None,",
                    f"    ) -> {result_type}:",
                ]
            )
        lines.extend(
            [
                f'        """{description(command, f"Send {domain_name}.{command_name}.")}"""',
                "",
            ]
        )
        call_params = "params" if parameters else "None"
        call_kwargs = "kwargs" if parameters else "{}"
        command_call = (
            f'await self._command("{command_name}", {call_params}, '
            f"session_id, {call_kwargs})"
        )
        if returns:
            lines.extend(
                [
                    f"        return cast({result_type}, {command_call})",
                ]
            )
        else:
            lines.append(f"        return {command_call}")

    for event in events:
        event_name = str(event["name"])
        parameters = object_list(event, "parameters")
        event_type = f"{title_name(event_name)}Event" if parameters else "JsonObject"
        lines.extend(
            [
                "",
                "    @overload",
                f"    def {event_name}(",
                "        self,",
                f"        callback_or_session: EventCallback[{event_type}],",
                "        handler: None = None,",
                "        *,",
                "        session_id: str | None = None,",
                "    ) -> Unsubscribe: ...",
                "",
                "    @overload",
                f"    def {event_name}(",
                "        self,",
                "        callback_or_session: str,",
                f"        handler: EventCallback[{event_type}],",
                "        *,",
                "        session_id: str | None = None,",
                "    ) -> Unsubscribe: ...",
                "",
                "    @overload",
                f"    def {event_name}(",
                "        self,",
                "        callback_or_session: str | None = None,",
                "        handler: None = None,",
                "        *,",
                "        session_id: str | None = None,",
                f"    ) -> Awaitable[{event_type}]: ...",
                "",
                f"    def {event_name}(",
                "        self,",
                f"        callback_or_session: EventCallback[{event_type}] | str | None = None,",
                f"        handler: EventCallback[{event_type}] | None = None,",
                "        *,",
                "        session_id: str | None = None,",
                f"    ) -> Awaitable[{event_type}] | Unsubscribe:",
                f'        """{description(event, f"Wait for or subscribe to {domain_name}.{event_name}.")}"""',
                "",
                (
                    "        return cast("
                    if event_type != "JsonObject"
                    else "        return self._event("
                ),
                *(
                    [f"            Awaitable[{event_type}] | Unsubscribe,"]
                    if event_type != "JsonObject"
                    else []
                ),
                "            self._event("
                if event_type != "JsonObject"
                else f'            "{event_name}",',
                *(
                    [f'                "{event_name}",']
                    if event_type != "JsonObject"
                    else []
                ),
                "                cast(EventCallback[Mapping[str, object]] | str | None, callback_or_session),",
                "                cast(EventCallback[Mapping[str, object]] | None, handler),",
                "                session_id,",
                *(["            ),"] if event_type != "JsonObject" else []),
                "        )",
            ]
        )

    lines.extend(["", "", f"__all__ = {sorted(exported, key=str.casefold)!r}", ""])
    return "\n".join(lines)


def _walk_dicts(value: JsonValue) -> list[JsonObject]:
    found: list[JsonObject] = []
    if isinstance(value, dict):
        found.append(value)
        for child in value.values():
            found.extend(_walk_dicts(child))
    elif isinstance(value, list):
        for child in value:
            found.extend(_walk_dicts(child))
    return found


def generate(protocol_path: Path, package_path: Path) -> None:
    descriptor = load_json_object(protocol_path)
    domains = object_list(descriptor, "domains")
    if not domains:
        raise ValueError(f"{protocol_path} has no domains array")
    destination = package_path / "domains"
    destination.mkdir(parents=True, exist_ok=True)
    expected: set[Path] = set()
    generated: dict[Path, str] = {}
    registry: list[tuple[str, str, str]] = []
    for raw_domain in domains:
        domain_name = str(raw_domain["domain"])
        module_name = snake_case(domain_name)
        output = destination / f"{module_name}.py"
        generated[output] = generate_domain(raw_domain)
        expected.add(output)
        type_names = {str(item["id"]) for item in object_list(raw_domain, "types")}
        class_name = (
            f"{domain_name}Domain" if domain_name in type_names else domain_name
        )
        registry.append((domain_name, module_name, class_name))
    init_lines = [
        '"""Generated CDP domain registry. Do not edit manually."""',
        "",
        "from __future__ import annotations",
        "",
        "from typing import TYPE_CHECKING",
        "",
        "from cdp.domain import Domain",
        "",
    ]
    for _domain_name, module_name, class_name in registry:
        init_lines.append(f"from .{module_name} import {class_name}")
    init_lines.extend(
        [
            "",
            "DOMAIN_CLASSES: dict[str, type[Domain]] = {",
            *[
                f'    "{domain_name}": {class_name},'
                for domain_name, _module_name, class_name in registry
            ],
            "}",
            "",
            "if TYPE_CHECKING:",
            "    _domain_count: int",
            "",
            f"__all__ = {sorted((item[2] for item in registry), key=str.casefold)!r}",
            "",
        ]
    )
    (destination / "__init__.py").write_text(
        "\n".join(init_lines),
        encoding="utf-8",
        newline="\n",
    )
    hint_lines = [
        '"""Generated client domain annotations. Do not edit manually."""',
        "",
        "from __future__ import annotations",
        "",
        "from typing import TYPE_CHECKING",
        "",
        "if TYPE_CHECKING:",
    ]
    for _domain_name, module_name, class_name in registry:
        hint_lines.append(f"    from .domains.{module_name} import {class_name}")
    hint_lines.extend(["", "", "class DomainHints:"])
    for domain_name, _module_name, class_name in registry:
        hint_lines.append(f"    {domain_name}: {class_name}")
    hint_lines.append("")
    for output, content in generated.items():
        output.write_text(content, encoding="utf-8", newline="\n")
    for old_module in destination.glob("*.py"):
        if old_module.name != "__init__.py" and old_module not in expected:
            old_module.unlink()
    (package_path / "_domain_hints.py").write_text(
        "\n".join(hint_lines),
        encoding="utf-8",
        newline="\n",
    )
    package_protocol = package_path / "protocol.json"
    if protocol_path.resolve() != package_protocol.resolve():
        shutil.copyfile(protocol_path, package_protocol)
    ruff = Path(sys.executable).with_name(
        "ruff.exe" if sys.platform == "win32" else "ruff"
    )
    if not ruff.is_file():
        ruff_on_path = shutil.which("ruff")
        if ruff_on_path is not None:
            ruff = Path(ruff_on_path)
    if ruff.is_file():
        subprocess.run(
            [str(ruff), "format", str(destination)],
            check=True,
        )
        subprocess.run(
            [str(ruff), "format", str(package_path / "_domain_hints.py")],
            check=True,
        )
        subprocess.run(
            [
                str(ruff),
                "check",
                "--fix",
                "--quiet",
                "--select",
                "F401,I001,RUF022,RUF068",
                str(destination),
                str(package_path / "_domain_hints.py"),
            ],
            check=True,
        )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "protocol",
        nargs="?",
        type=Path,
        default=DEFAULT_PROTOCOL,
        help="input protocol.json",
    )
    parser.add_argument(
        "--package",
        type=Path,
        default=DEFAULT_PACKAGE,
        help="destination Python package",
    )
    arguments = parser.parse_args()
    generate(arguments.protocol.resolve(), arguments.package.resolve())


if __name__ == "__main__":
    main()
