"""Command-line interface compatible with chrome-remote-interface's utilities."""

from __future__ import annotations

import argparse
import asyncio
import codeop
import inspect
import json
from collections.abc import Awaitable
from importlib.metadata import PackageNotFoundError
from importlib.metadata import version as package_version
from pathlib import Path
from typing import cast

from typing_extensions import TypedDict

from . import Activate, Close, List, New, Protocol, Version, connect
from .types import ProtocolDescriptor, to_json_value


class CommonOptions(TypedDict):
    host: str
    port: int
    secure: bool
    use_host_name: bool


def _common_options(arguments: argparse.Namespace) -> CommonOptions:
    return {
        "host": arguments.host,
        "port": arguments.port,
        "secure": arguments.secure,
        "use_host_name": arguments.use_host_name,
    }


async def _inspect(arguments: argparse.Namespace) -> None:
    options = _common_options(arguments)
    target: str | None = arguments.target
    descriptor: ProtocolDescriptor | None = None
    if arguments.protocol_file:
        protocol_text = await asyncio.to_thread(
            Path(arguments.protocol_file).read_text,
            encoding="utf-8",
        )
        raw_descriptor: object = json.loads(protocol_text)
        normalized_descriptor = to_json_value(raw_descriptor)
        if not isinstance(normalized_descriptor, dict):
            raise TypeError("protocol file must contain a JSON object")
        descriptor = normalized_descriptor
    client = await connect(
        target,
        **options,
        local=arguments.local,
        protocol=descriptor,
    )
    namespace = {
        name: getattr(client, name) for name in vars(client) if name[:1].isupper()
    }
    namespace["client"] = client
    print("Connected. CDP domains and `client` are available; awaitables are awaited.")
    compiler = codeop.CommandCompiler()
    try:
        while True:
            try:
                source = await asyncio.to_thread(input, ">>> ")
            except (EOFError, KeyboardInterrupt):
                print()
                break
            if source.strip() in {".exit", "exit", "quit"}:
                break
            if source.strip() == ".target":
                print(client.webSocketUrl)
                continue
            if source.strip() == ".reset":
                client.remove_all_listeners()
                continue
            try:
                expression = compile(source, "<cdp>", "eval")
            except SyntaxError:
                statement = compiler(source, "<cdp>", "exec")
                if statement is None:
                    print("Multiline statements are not supported by this shell.")
                    continue
                try:
                    exec(statement, namespace)
                except Exception as error:
                    print(f"{type(error).__name__}: {error}")
                continue
            try:
                result = eval(expression, namespace)
                if inspect.isawaitable(result):
                    result = await cast(Awaitable[object], result)
                if result is not None:
                    print(repr(result))
            except Exception as error:
                print(f"{type(error).__name__}: {error}")
    finally:
        await client.close()


async def _run(arguments: argparse.Namespace) -> None:
    options: dict[str, object] = dict(_common_options(arguments))
    if arguments.command == "inspect":
        await _inspect(arguments)
    elif arguments.command == "list":
        print(json.dumps(await List(options), indent=4))
    elif arguments.command == "new":
        if arguments.url is not None:
            options["url"] = arguments.url
        print(json.dumps(await New(options), indent=4))
    elif arguments.command == "activate":
        await Activate({**options, "id": arguments.id})
    elif arguments.command == "close":
        await Close({**options, "id": arguments.id})
    elif arguments.command == "version":
        print(json.dumps(await Version(options), indent=4))
    elif arguments.command == "protocol":
        options["local"] = arguments.local
        print(json.dumps(await Protocol(options), indent=4))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="chrome-remote-interface")
    parser.add_argument("-t", "--host", default="localhost")
    parser.add_argument("-p", "--port", type=int, default=9222)
    parser.add_argument("-s", "--secure", action="store_true")
    parser.add_argument("-n", "--use-host-name", action="store_true")
    parser.add_argument("--version", action="store_true", dest="show_version")
    commands = parser.add_subparsers(dest="command")

    inspect_parser = commands.add_parser("inspect")
    inspect_parser.add_argument("target", nargs="?")
    inspect_parser.add_argument("-w", "--web-socket", action="store_true")
    inspect_parser.add_argument("-j", "--protocol", dest="protocol_file")
    inspect_parser.add_argument("-l", "--local", action="store_true")

    commands.add_parser("list")
    new_parser = commands.add_parser("new")
    new_parser.add_argument("url", nargs="?")
    activate_parser = commands.add_parser("activate")
    activate_parser.add_argument("id")
    close_parser = commands.add_parser("close")
    close_parser.add_argument("id")
    commands.add_parser("version")
    protocol_parser = commands.add_parser("protocol")
    protocol_parser.add_argument("-l", "--local", action="store_true")
    return parser


def main() -> None:
    parser = build_parser()
    arguments = parser.parse_args()
    if arguments.show_version:
        try:
            print(package_version("chrome-remote-interface"))
        except PackageNotFoundError:
            print("unknown")
        return
    if arguments.command is None:
        parser.print_help()
        parser.exit(1)
    asyncio.run(_run(arguments))


if __name__ == "__main__":
    main()
