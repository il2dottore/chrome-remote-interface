"""Generated bindings for the CDP CSS domain. Do not edit manually."""

from __future__ import annotations

from collections.abc import Awaitable, Mapping
from typing import TYPE_CHECKING, Literal, TypeAlias, cast, overload

from typing_extensions import NotRequired, TypedDict, Unpack

from cdp.domain import Domain as BaseDomain, EventCallback, Unsubscribe
from cdp.types import JsonObject

if TYPE_CHECKING:
    from . import dom as DOM
    from . import page as Page


StyleSheetOrigin: TypeAlias = Literal["injected", "user-agent", "inspector", "regular"]


class PseudoElementMatches(TypedDict):
    pseudoType: DOM.PseudoType
    pseudoIdentifier: NotRequired[str]
    matches: list[RuleMatch]


class CSSAnimationStyle(TypedDict):
    name: NotRequired[str]
    style: CSSStyle


class InheritedStyleEntry(TypedDict):
    inlineStyle: NotRequired[CSSStyle]
    matchedCSSRules: list[RuleMatch]


class InheritedAnimatedStyleEntry(TypedDict):
    animationStyles: NotRequired[list[CSSAnimationStyle]]
    transitionsStyle: NotRequired[CSSStyle]


class InheritedPseudoElementMatches(TypedDict):
    pseudoElements: list[PseudoElementMatches]


class RuleMatch(TypedDict):
    rule: CSSRule
    matchingSelectors: list[int]


class Value(TypedDict):
    text: str
    range: NotRequired[SourceRange]
    specificity: NotRequired[Specificity]


class SpecificityComponent(TypedDict):
    text: str
    a: int
    b: int
    c: int


class Specificity(TypedDict):
    a: int
    b: int
    c: int
    components: NotRequired[list[SpecificityComponent]]


class SelectorList(TypedDict):
    selectors: list[Value]
    text: str


class CSSStyleSheetHeader(TypedDict):
    styleSheetId: DOM.StyleSheetId
    frameId: Page.FrameId
    sourceURL: str
    sourceMapURL: NotRequired[str]
    origin: StyleSheetOrigin
    title: str
    ownerNode: NotRequired[DOM.BackendNodeId]
    disabled: bool
    hasSourceURL: NotRequired[bool]
    isInline: bool
    isMutable: bool
    isConstructed: bool
    startLine: float
    startColumn: float
    length: float
    endLine: float
    endColumn: float
    loadingFailed: NotRequired[bool]


class CSSRule(TypedDict):
    styleSheetId: NotRequired[DOM.StyleSheetId]
    selectorList: SelectorList
    nestingSelectors: NotRequired[list[str]]
    origin: StyleSheetOrigin
    style: CSSStyle
    originTreeScopeNodeId: NotRequired[DOM.BackendNodeId]
    media: NotRequired[list[CSSMedia]]
    containerQueries: NotRequired[list[CSSContainerQuery]]
    supports: NotRequired[list[CSSSupports]]
    layers: NotRequired[list[CSSLayer]]
    scopes: NotRequired[list[CSSScope]]
    ruleTypes: NotRequired[list[CSSRuleType]]
    startingStyles: NotRequired[list[CSSStartingStyle]]
    navigations: NotRequired[list[CSSNavigation]]


CSSRuleType: TypeAlias = Literal[
    "MediaRule",
    "SupportsRule",
    "ContainerRule",
    "LayerRule",
    "ScopeRule",
    "StyleRule",
    "StartingStyleRule",
    "NavigationRule",
]


class RuleUsage(TypedDict):
    styleSheetId: DOM.StyleSheetId
    startOffset: float
    endOffset: float
    used: bool


class SourceRange(TypedDict):
    startLine: int
    startColumn: int
    endLine: int
    endColumn: int


class ShorthandEntry(TypedDict):
    name: str
    value: str
    important: NotRequired[bool]


class CSSComputedStyleProperty(TypedDict):
    name: str
    value: str


class ComputedStyleExtraFields(TypedDict):
    isAppearanceBase: bool


class CSSStyle(TypedDict):
    styleSheetId: NotRequired[DOM.StyleSheetId]
    cssProperties: list[CSSProperty]
    shorthandEntries: list[ShorthandEntry]
    cssText: NotRequired[str]
    range: NotRequired[SourceRange]


class CSSProperty(TypedDict):
    name: str
    value: str
    important: NotRequired[bool]
    implicit: NotRequired[bool]
    text: NotRequired[str]
    parsedOk: NotRequired[bool]
    disabled: NotRequired[bool]
    range: NotRequired[SourceRange]
    longhandProperties: NotRequired[list[CSSProperty]]


class CSSMedia(TypedDict):
    text: str
    source: Literal["mediaRule", "importRule", "linkedSheet", "inlineSheet"]
    sourceURL: NotRequired[str]
    range: NotRequired[SourceRange]
    styleSheetId: NotRequired[DOM.StyleSheetId]
    mediaList: NotRequired[list[MediaQuery]]


class MediaQuery(TypedDict):
    expressions: list[MediaQueryExpression]
    active: bool


class MediaQueryExpression(TypedDict):
    value: float
    unit: str
    feature: str
    valueRange: NotRequired[SourceRange]
    computedLength: NotRequired[float]


class CSSContainerQuery(TypedDict):
    text: str
    range: NotRequired[SourceRange]
    styleSheetId: NotRequired[DOM.StyleSheetId]
    name: NotRequired[str]
    physicalAxes: NotRequired[DOM.PhysicalAxes]
    logicalAxes: NotRequired[DOM.LogicalAxes]
    queriesScrollState: NotRequired[bool]
    queriesAnchored: NotRequired[bool]
    conditionText: str


class CSSSupports(TypedDict):
    text: str
    active: bool
    range: NotRequired[SourceRange]
    styleSheetId: NotRequired[DOM.StyleSheetId]


class CSSNavigation(TypedDict):
    text: str
    active: NotRequired[bool]
    range: NotRequired[SourceRange]
    styleSheetId: NotRequired[DOM.StyleSheetId]


class CSSScope(TypedDict):
    text: str
    range: NotRequired[SourceRange]
    styleSheetId: NotRequired[DOM.StyleSheetId]


class CSSLayer(TypedDict):
    text: str
    range: NotRequired[SourceRange]
    styleSheetId: NotRequired[DOM.StyleSheetId]


class CSSStartingStyle(TypedDict):
    range: NotRequired[SourceRange]
    styleSheetId: NotRequired[DOM.StyleSheetId]


class CSSLayerData(TypedDict):
    name: str
    subLayers: NotRequired[list[CSSLayerData]]
    order: float


class PlatformFontUsage(TypedDict):
    familyName: str
    postScriptName: str
    isCustomFont: bool
    glyphCount: float


class FontVariationAxis(TypedDict):
    tag: str
    name: str
    minValue: float
    maxValue: float
    defaultValue: float


class FontFace(TypedDict):
    fontFamily: str
    fontStyle: str
    fontVariant: str
    fontWeight: str
    fontStretch: str
    fontDisplay: str
    unicodeRange: str
    src: str
    platformFontFamily: str
    fontVariationAxes: NotRequired[list[FontVariationAxis]]


class CSSTryRule(TypedDict):
    styleSheetId: NotRequired[DOM.StyleSheetId]
    origin: StyleSheetOrigin
    style: CSSStyle


class CSSPositionTryRule(TypedDict):
    name: Value
    styleSheetId: NotRequired[DOM.StyleSheetId]
    origin: StyleSheetOrigin
    style: CSSStyle
    active: bool


class CSSKeyframesRule(TypedDict):
    animationName: Value
    keyframes: list[CSSKeyframeRule]


class CSSPropertyRegistration(TypedDict):
    propertyName: str
    initialValue: NotRequired[Value]
    inherits: bool
    syntax: str


class CSSAtRule(TypedDict):
    type: Literal[
        "font-face", "font-feature-values", "font-palette-values", "counter-style"
    ]
    subsection: NotRequired[
        Literal[
            "swash",
            "annotation",
            "ornaments",
            "stylistic",
            "styleset",
            "character-variant",
        ]
    ]
    name: NotRequired[Value]
    styleSheetId: NotRequired[DOM.StyleSheetId]
    origin: StyleSheetOrigin
    style: CSSStyle


class CSSPropertyRule(TypedDict):
    styleSheetId: NotRequired[DOM.StyleSheetId]
    origin: StyleSheetOrigin
    propertyName: Value
    style: CSSStyle


class CSSFunctionParameter(TypedDict):
    name: str
    type: str


class CSSFunctionConditionNode(TypedDict):
    media: NotRequired[CSSMedia]
    containerQueries: NotRequired[CSSContainerQuery]
    supports: NotRequired[CSSSupports]
    navigation: NotRequired[CSSNavigation]
    children: list[CSSFunctionNode]
    conditionText: str


class CSSFunctionNode(TypedDict):
    condition: NotRequired[CSSFunctionConditionNode]
    style: NotRequired[CSSStyle]


class CSSFunctionRule(TypedDict):
    name: Value
    styleSheetId: NotRequired[DOM.StyleSheetId]
    origin: StyleSheetOrigin
    parameters: list[CSSFunctionParameter]
    children: list[CSSFunctionNode]
    originTreeScopeNodeId: NotRequired[DOM.BackendNodeId]


class CSSKeyframeRule(TypedDict):
    styleSheetId: NotRequired[DOM.StyleSheetId]
    origin: StyleSheetOrigin
    keyText: Value
    style: CSSStyle


class StyleDeclarationEdit(TypedDict):
    styleSheetId: DOM.StyleSheetId
    range: SourceRange
    text: str


class AddRuleParameters(TypedDict):
    styleSheetId: DOM.StyleSheetId
    ruleText: str
    location: SourceRange
    nodeForPropertySyntaxValidation: NotRequired[DOM.NodeId]


class AddRuleResult(TypedDict):
    rule: CSSRule


class CollectClassNamesParameters(TypedDict):
    styleSheetId: DOM.StyleSheetId


class CollectClassNamesResult(TypedDict):
    classNames: list[str]


class CreateStyleSheetParameters(TypedDict):
    frameId: Page.FrameId
    force: NotRequired[bool]


class CreateStyleSheetResult(TypedDict):
    styleSheetId: DOM.StyleSheetId


class ForcePseudoStateParameters(TypedDict):
    nodeId: DOM.NodeId
    forcedPseudoClasses: list[str]


class ForceStartingStyleParameters(TypedDict):
    nodeId: DOM.NodeId
    forced: bool


class GetBackgroundColorsParameters(TypedDict):
    nodeId: DOM.NodeId


class GetBackgroundColorsResult(TypedDict):
    backgroundColors: NotRequired[list[str]]
    computedFontSize: NotRequired[str]
    computedFontWeight: NotRequired[str]


class GetComputedStyleForNodeParameters(TypedDict):
    nodeId: DOM.NodeId


class GetComputedStyleForNodeResult(TypedDict):
    computedStyle: list[CSSComputedStyleProperty]
    extraFields: ComputedStyleExtraFields


class ResolveValuesParameters(TypedDict):
    values: list[str]
    nodeId: DOM.NodeId
    propertyName: NotRequired[str]
    pseudoType: NotRequired[DOM.PseudoType]
    pseudoIdentifier: NotRequired[str]


class ResolveValuesResult(TypedDict):
    results: list[str]


class GetLonghandPropertiesParameters(TypedDict):
    shorthandName: str
    value: str


class GetLonghandPropertiesResult(TypedDict):
    longhandProperties: list[CSSProperty]


class GetInlineStylesForNodeParameters(TypedDict):
    nodeId: DOM.NodeId


class GetInlineStylesForNodeResult(TypedDict):
    inlineStyle: NotRequired[CSSStyle]
    attributesStyle: NotRequired[CSSStyle]


class GetAnimatedStylesForNodeParameters(TypedDict):
    nodeId: DOM.NodeId


class GetAnimatedStylesForNodeResult(TypedDict):
    animationStyles: NotRequired[list[CSSAnimationStyle]]
    transitionsStyle: NotRequired[CSSStyle]
    inherited: NotRequired[list[InheritedAnimatedStyleEntry]]


class GetMatchedStylesForNodeParameters(TypedDict):
    nodeId: DOM.NodeId


class GetMatchedStylesForNodeResult(TypedDict):
    inlineStyle: NotRequired[CSSStyle]
    attributesStyle: NotRequired[CSSStyle]
    matchedCSSRules: NotRequired[list[RuleMatch]]
    pseudoElements: NotRequired[list[PseudoElementMatches]]
    inherited: NotRequired[list[InheritedStyleEntry]]
    inheritedPseudoElements: NotRequired[list[InheritedPseudoElementMatches]]
    cssKeyframesRules: NotRequired[list[CSSKeyframesRule]]
    cssPositionTryRules: NotRequired[list[CSSPositionTryRule]]
    activePositionFallbackIndex: NotRequired[int]
    cssPropertyRules: NotRequired[list[CSSPropertyRule]]
    cssPropertyRegistrations: NotRequired[list[CSSPropertyRegistration]]
    cssAtRules: NotRequired[list[CSSAtRule]]
    parentLayoutNodeId: NotRequired[DOM.NodeId]
    cssFunctionRules: NotRequired[list[CSSFunctionRule]]


class GetEnvironmentVariablesResult(TypedDict):
    environmentVariables: JsonObject


class GetMediaQueriesResult(TypedDict):
    medias: list[CSSMedia]


class GetPlatformFontsForNodeParameters(TypedDict):
    nodeId: DOM.NodeId


class GetPlatformFontsForNodeResult(TypedDict):
    fonts: list[PlatformFontUsage]


class GetStyleSheetTextParameters(TypedDict):
    styleSheetId: DOM.StyleSheetId


class GetStyleSheetTextResult(TypedDict):
    text: str


class GetLayersForNodeParameters(TypedDict):
    nodeId: DOM.NodeId


class GetLayersForNodeResult(TypedDict):
    rootLayer: CSSLayerData


class GetLocationForSelectorParameters(TypedDict):
    styleSheetId: DOM.StyleSheetId
    selectorText: str


class GetLocationForSelectorResult(TypedDict):
    ranges: list[SourceRange]


class TrackComputedStyleUpdatesForNodeParameters(TypedDict):
    nodeId: NotRequired[DOM.NodeId]


class TrackComputedStyleUpdatesParameters(TypedDict):
    propertiesToTrack: list[CSSComputedStyleProperty]


class TakeComputedStyleUpdatesResult(TypedDict):
    nodeIds: list[DOM.NodeId]


class SetEffectivePropertyValueForNodeParameters(TypedDict):
    nodeId: DOM.NodeId
    propertyName: str
    value: str


class SetPropertyRulePropertyNameParameters(TypedDict):
    styleSheetId: DOM.StyleSheetId
    range: SourceRange
    propertyName: str


class SetPropertyRulePropertyNameResult(TypedDict):
    propertyName: Value


class SetKeyframeKeyParameters(TypedDict):
    styleSheetId: DOM.StyleSheetId
    range: SourceRange
    keyText: str


class SetKeyframeKeyResult(TypedDict):
    keyText: Value


class SetMediaTextParameters(TypedDict):
    styleSheetId: DOM.StyleSheetId
    range: SourceRange
    text: str


class SetMediaTextResult(TypedDict):
    media: CSSMedia


class SetContainerQueryTextParameters(TypedDict):
    styleSheetId: DOM.StyleSheetId
    range: SourceRange
    text: str


class SetContainerQueryTextResult(TypedDict):
    containerQuery: CSSContainerQuery


class SetContainerQueryConditionTextParameters(TypedDict):
    styleSheetId: DOM.StyleSheetId
    range: SourceRange
    text: str


class SetContainerQueryConditionTextResult(TypedDict):
    containerQuery: CSSContainerQuery


class SetSupportsTextParameters(TypedDict):
    styleSheetId: DOM.StyleSheetId
    range: SourceRange
    text: str


class SetSupportsTextResult(TypedDict):
    supports: CSSSupports


class SetNavigationTextParameters(TypedDict):
    styleSheetId: DOM.StyleSheetId
    range: SourceRange
    text: str


class SetNavigationTextResult(TypedDict):
    navigation: CSSNavigation


class SetScopeTextParameters(TypedDict):
    styleSheetId: DOM.StyleSheetId
    range: SourceRange
    text: str


class SetScopeTextResult(TypedDict):
    scope: CSSScope


class SetRuleSelectorParameters(TypedDict):
    styleSheetId: DOM.StyleSheetId
    range: SourceRange
    selector: str


class SetRuleSelectorResult(TypedDict):
    selectorList: SelectorList


class SetStyleSheetTextParameters(TypedDict):
    styleSheetId: DOM.StyleSheetId
    text: str


class SetStyleSheetTextResult(TypedDict):
    sourceMapURL: NotRequired[str]


class SetStyleTextsParameters(TypedDict):
    edits: list[StyleDeclarationEdit]
    nodeForPropertySyntaxValidation: NotRequired[DOM.NodeId]


class SetStyleTextsResult(TypedDict):
    styles: list[CSSStyle]


class StopRuleUsageTrackingResult(TypedDict):
    ruleUsage: list[RuleUsage]


class TakeCoverageDeltaResult(TypedDict):
    coverage: list[RuleUsage]
    timestamp: float


class SetLocalFontsEnabledParameters(TypedDict):
    enabled: bool


class FontsUpdatedEvent(TypedDict):
    font: NotRequired[FontFace]


class StyleSheetAddedEvent(TypedDict):
    header: CSSStyleSheetHeader


class StyleSheetChangedEvent(TypedDict):
    styleSheetId: DOM.StyleSheetId


class StyleSheetRemovedEvent(TypedDict):
    styleSheetId: DOM.StyleSheetId


class ComputedStyleUpdatedEvent(TypedDict):
    nodeId: DOM.NodeId


class CSS(BaseDomain):
    """This domain exposes CSS read/write operations. All CSS objects (stylesheets, rules, and styles) have an associated `id` used in subsequent operations on the related object. Each object type has a specific `id` structure, and those are not interchangeable between objects of different kinds. CSS objects can be loaded using the `get*ForNode()` calls (which accept a DOM node id). A client can also keep track of stylesheets via the `styleSheetAdded`/`styleSheetRemoved` events and subsequently load the required stylesheet contents using the `getStyleSheet[Text]()` methods."""

    domain_name = "CSS"

    @overload
    async def addRule(
        self,
        params: AddRuleParameters,
        session_id: str | None = None,
    ) -> AddRuleResult: ...

    @overload
    async def addRule(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[AddRuleParameters],
    ) -> AddRuleResult: ...

    async def addRule(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> AddRuleResult:
        """Inserts a new rule with the given `ruleText` in a stylesheet with given `styleSheetId`, at the position specified by `location`."""

        return cast(
            AddRuleResult, await self._command("addRule", params, session_id, kwargs)
        )

    @overload
    async def collectClassNames(
        self,
        params: CollectClassNamesParameters,
        session_id: str | None = None,
    ) -> CollectClassNamesResult: ...

    @overload
    async def collectClassNames(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[CollectClassNamesParameters],
    ) -> CollectClassNamesResult: ...

    async def collectClassNames(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> CollectClassNamesResult:
        """Returns all class names from specified stylesheet."""

        return cast(
            CollectClassNamesResult,
            await self._command("collectClassNames", params, session_id, kwargs),
        )

    @overload
    async def createStyleSheet(
        self,
        params: CreateStyleSheetParameters,
        session_id: str | None = None,
    ) -> CreateStyleSheetResult: ...

    @overload
    async def createStyleSheet(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[CreateStyleSheetParameters],
    ) -> CreateStyleSheetResult: ...

    async def createStyleSheet(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> CreateStyleSheetResult:
        """Creates a new special "via-inspector" stylesheet in the frame with given `frameId`."""

        return cast(
            CreateStyleSheetResult,
            await self._command("createStyleSheet", params, session_id, kwargs),
        )

    async def disable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Disables the CSS agent for the given page."""

        return await self._command("disable", None, session_id, {})

    async def enable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Enables the CSS agent for the given page. Clients should not assume that the CSS agent has been enabled until the result of this command is received."""

        return await self._command("enable", None, session_id, {})

    @overload
    async def forcePseudoState(
        self,
        params: ForcePseudoStateParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def forcePseudoState(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[ForcePseudoStateParameters],
    ) -> JsonObject: ...

    async def forcePseudoState(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Ensures that the given node will have specified pseudo-classes whenever its style is computed by the browser."""

        return await self._command("forcePseudoState", params, session_id, kwargs)

    @overload
    async def forceStartingStyle(
        self,
        params: ForceStartingStyleParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def forceStartingStyle(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[ForceStartingStyleParameters],
    ) -> JsonObject: ...

    async def forceStartingStyle(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Ensures that the given node is in its starting-style state."""

        return await self._command("forceStartingStyle", params, session_id, kwargs)

    @overload
    async def getBackgroundColors(
        self,
        params: GetBackgroundColorsParameters,
        session_id: str | None = None,
    ) -> GetBackgroundColorsResult: ...

    @overload
    async def getBackgroundColors(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetBackgroundColorsParameters],
    ) -> GetBackgroundColorsResult: ...

    async def getBackgroundColors(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetBackgroundColorsResult:
        """Send CSS.getBackgroundColors."""

        return cast(
            GetBackgroundColorsResult,
            await self._command("getBackgroundColors", params, session_id, kwargs),
        )

    @overload
    async def getComputedStyleForNode(
        self,
        params: GetComputedStyleForNodeParameters,
        session_id: str | None = None,
    ) -> GetComputedStyleForNodeResult: ...

    @overload
    async def getComputedStyleForNode(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetComputedStyleForNodeParameters],
    ) -> GetComputedStyleForNodeResult: ...

    async def getComputedStyleForNode(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetComputedStyleForNodeResult:
        """Returns the computed style for a DOM node identified by `nodeId`."""

        return cast(
            GetComputedStyleForNodeResult,
            await self._command("getComputedStyleForNode", params, session_id, kwargs),
        )

    @overload
    async def resolveValues(
        self,
        params: ResolveValuesParameters,
        session_id: str | None = None,
    ) -> ResolveValuesResult: ...

    @overload
    async def resolveValues(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[ResolveValuesParameters],
    ) -> ResolveValuesResult: ...

    async def resolveValues(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> ResolveValuesResult:
        """Resolve the specified values in the context of the provided element. For example, a value of '1em' is evaluated according to the computed 'font-size' of the element and a value 'calc(1px + 2px)' will be resolved to '3px'. If the `propertyName` was specified the `values` are resolved as if they were property's declaration. If a value cannot be parsed according to the provided property syntax, the value is parsed using combined syntax as if null `propertyName` was provided. If the value cannot be resolved even then, return the provided value without any changes. Note: this function currently does not resolve CSS random() function, it returns unmodified random() function parts.`"""

        return cast(
            ResolveValuesResult,
            await self._command("resolveValues", params, session_id, kwargs),
        )

    @overload
    async def getLonghandProperties(
        self,
        params: GetLonghandPropertiesParameters,
        session_id: str | None = None,
    ) -> GetLonghandPropertiesResult: ...

    @overload
    async def getLonghandProperties(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetLonghandPropertiesParameters],
    ) -> GetLonghandPropertiesResult: ...

    async def getLonghandProperties(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetLonghandPropertiesResult:
        """Send CSS.getLonghandProperties."""

        return cast(
            GetLonghandPropertiesResult,
            await self._command("getLonghandProperties", params, session_id, kwargs),
        )

    @overload
    async def getInlineStylesForNode(
        self,
        params: GetInlineStylesForNodeParameters,
        session_id: str | None = None,
    ) -> GetInlineStylesForNodeResult: ...

    @overload
    async def getInlineStylesForNode(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetInlineStylesForNodeParameters],
    ) -> GetInlineStylesForNodeResult: ...

    async def getInlineStylesForNode(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetInlineStylesForNodeResult:
        """Returns the styles defined inline (explicitly in the "style" attribute and implicitly, using DOM attributes) for a DOM node identified by `nodeId`."""

        return cast(
            GetInlineStylesForNodeResult,
            await self._command("getInlineStylesForNode", params, session_id, kwargs),
        )

    @overload
    async def getAnimatedStylesForNode(
        self,
        params: GetAnimatedStylesForNodeParameters,
        session_id: str | None = None,
    ) -> GetAnimatedStylesForNodeResult: ...

    @overload
    async def getAnimatedStylesForNode(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetAnimatedStylesForNodeParameters],
    ) -> GetAnimatedStylesForNodeResult: ...

    async def getAnimatedStylesForNode(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetAnimatedStylesForNodeResult:
        """Returns the styles coming from animations & transitions including the animation & transition styles coming from inheritance chain."""

        return cast(
            GetAnimatedStylesForNodeResult,
            await self._command("getAnimatedStylesForNode", params, session_id, kwargs),
        )

    @overload
    async def getMatchedStylesForNode(
        self,
        params: GetMatchedStylesForNodeParameters,
        session_id: str | None = None,
    ) -> GetMatchedStylesForNodeResult: ...

    @overload
    async def getMatchedStylesForNode(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetMatchedStylesForNodeParameters],
    ) -> GetMatchedStylesForNodeResult: ...

    async def getMatchedStylesForNode(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetMatchedStylesForNodeResult:
        """Returns requested styles for a DOM node identified by `nodeId`."""

        return cast(
            GetMatchedStylesForNodeResult,
            await self._command("getMatchedStylesForNode", params, session_id, kwargs),
        )

    async def getEnvironmentVariables(
        self,
        session_id: str | None = None,
    ) -> GetEnvironmentVariablesResult:
        """Returns the values of the default UA-defined environment variables used in env()"""

        return cast(
            GetEnvironmentVariablesResult,
            await self._command("getEnvironmentVariables", None, session_id, {}),
        )

    async def getMediaQueries(
        self,
        session_id: str | None = None,
    ) -> GetMediaQueriesResult:
        """Returns all media queries parsed by the rendering engine."""

        return cast(
            GetMediaQueriesResult,
            await self._command("getMediaQueries", None, session_id, {}),
        )

    @overload
    async def getPlatformFontsForNode(
        self,
        params: GetPlatformFontsForNodeParameters,
        session_id: str | None = None,
    ) -> GetPlatformFontsForNodeResult: ...

    @overload
    async def getPlatformFontsForNode(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetPlatformFontsForNodeParameters],
    ) -> GetPlatformFontsForNodeResult: ...

    async def getPlatformFontsForNode(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetPlatformFontsForNodeResult:
        """Requests information about platform fonts which we used to render child TextNodes in the given node."""

        return cast(
            GetPlatformFontsForNodeResult,
            await self._command("getPlatformFontsForNode", params, session_id, kwargs),
        )

    @overload
    async def getStyleSheetText(
        self,
        params: GetStyleSheetTextParameters,
        session_id: str | None = None,
    ) -> GetStyleSheetTextResult: ...

    @overload
    async def getStyleSheetText(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetStyleSheetTextParameters],
    ) -> GetStyleSheetTextResult: ...

    async def getStyleSheetText(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetStyleSheetTextResult:
        """Returns the current textual content for a stylesheet."""

        return cast(
            GetStyleSheetTextResult,
            await self._command("getStyleSheetText", params, session_id, kwargs),
        )

    @overload
    async def getLayersForNode(
        self,
        params: GetLayersForNodeParameters,
        session_id: str | None = None,
    ) -> GetLayersForNodeResult: ...

    @overload
    async def getLayersForNode(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetLayersForNodeParameters],
    ) -> GetLayersForNodeResult: ...

    async def getLayersForNode(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetLayersForNodeResult:
        """Returns all layers parsed by the rendering engine for the tree scope of a node. Given a DOM element identified by nodeId, getLayersForNode returns the root layer for the nearest ancestor document or shadow root. The layer root contains the full layer tree for the tree scope and their ordering."""

        return cast(
            GetLayersForNodeResult,
            await self._command("getLayersForNode", params, session_id, kwargs),
        )

    @overload
    async def getLocationForSelector(
        self,
        params: GetLocationForSelectorParameters,
        session_id: str | None = None,
    ) -> GetLocationForSelectorResult: ...

    @overload
    async def getLocationForSelector(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetLocationForSelectorParameters],
    ) -> GetLocationForSelectorResult: ...

    async def getLocationForSelector(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetLocationForSelectorResult:
        """Given a CSS selector text and a style sheet ID, getLocationForSelector returns an array of locations of the CSS selector in the style sheet."""

        return cast(
            GetLocationForSelectorResult,
            await self._command("getLocationForSelector", params, session_id, kwargs),
        )

    @overload
    async def trackComputedStyleUpdatesForNode(
        self,
        params: TrackComputedStyleUpdatesForNodeParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def trackComputedStyleUpdatesForNode(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[TrackComputedStyleUpdatesForNodeParameters],
    ) -> JsonObject: ...

    async def trackComputedStyleUpdatesForNode(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Starts tracking the given node for the computed style updates and whenever the computed style is updated for node, it queues a `computedStyleUpdated` event with throttling. There can only be 1 node tracked for computed style updates so passing a new node id removes tracking from the previous node. Pass `undefined` to disable tracking."""

        return await self._command(
            "trackComputedStyleUpdatesForNode", params, session_id, kwargs
        )

    @overload
    async def trackComputedStyleUpdates(
        self,
        params: TrackComputedStyleUpdatesParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def trackComputedStyleUpdates(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[TrackComputedStyleUpdatesParameters],
    ) -> JsonObject: ...

    async def trackComputedStyleUpdates(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Starts tracking the given computed styles for updates. The specified array of properties replaces the one previously specified. Pass empty array to disable tracking. Use takeComputedStyleUpdates to retrieve the list of nodes that had properties modified. The changes to computed style properties are only tracked for nodes pushed to the front-end by the DOM agent. If no changes to the tracked properties occur after the node has been pushed to the front-end, no updates will be issued for the node."""

        return await self._command(
            "trackComputedStyleUpdates", params, session_id, kwargs
        )

    async def takeComputedStyleUpdates(
        self,
        session_id: str | None = None,
    ) -> TakeComputedStyleUpdatesResult:
        """Polls the next batch of computed style updates."""

        return cast(
            TakeComputedStyleUpdatesResult,
            await self._command("takeComputedStyleUpdates", None, session_id, {}),
        )

    @overload
    async def setEffectivePropertyValueForNode(
        self,
        params: SetEffectivePropertyValueForNodeParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setEffectivePropertyValueForNode(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetEffectivePropertyValueForNodeParameters],
    ) -> JsonObject: ...

    async def setEffectivePropertyValueForNode(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Find a rule with the given active property for the given node and set the new value for this property"""

        return await self._command(
            "setEffectivePropertyValueForNode", params, session_id, kwargs
        )

    @overload
    async def setPropertyRulePropertyName(
        self,
        params: SetPropertyRulePropertyNameParameters,
        session_id: str | None = None,
    ) -> SetPropertyRulePropertyNameResult: ...

    @overload
    async def setPropertyRulePropertyName(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetPropertyRulePropertyNameParameters],
    ) -> SetPropertyRulePropertyNameResult: ...

    async def setPropertyRulePropertyName(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> SetPropertyRulePropertyNameResult:
        """Modifies the property rule property name."""

        return cast(
            SetPropertyRulePropertyNameResult,
            await self._command(
                "setPropertyRulePropertyName", params, session_id, kwargs
            ),
        )

    @overload
    async def setKeyframeKey(
        self,
        params: SetKeyframeKeyParameters,
        session_id: str | None = None,
    ) -> SetKeyframeKeyResult: ...

    @overload
    async def setKeyframeKey(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetKeyframeKeyParameters],
    ) -> SetKeyframeKeyResult: ...

    async def setKeyframeKey(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> SetKeyframeKeyResult:
        """Modifies the keyframe rule key text."""

        return cast(
            SetKeyframeKeyResult,
            await self._command("setKeyframeKey", params, session_id, kwargs),
        )

    @overload
    async def setMediaText(
        self,
        params: SetMediaTextParameters,
        session_id: str | None = None,
    ) -> SetMediaTextResult: ...

    @overload
    async def setMediaText(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetMediaTextParameters],
    ) -> SetMediaTextResult: ...

    async def setMediaText(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> SetMediaTextResult:
        """Modifies the rule selector."""

        return cast(
            SetMediaTextResult,
            await self._command("setMediaText", params, session_id, kwargs),
        )

    @overload
    async def setContainerQueryText(
        self,
        params: SetContainerQueryTextParameters,
        session_id: str | None = None,
    ) -> SetContainerQueryTextResult: ...

    @overload
    async def setContainerQueryText(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetContainerQueryTextParameters],
    ) -> SetContainerQueryTextResult: ...

    async def setContainerQueryText(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> SetContainerQueryTextResult:
        """Modifies the expression of a container query. Deprecated. Use setContainerQueryConditionText instead."""

        return cast(
            SetContainerQueryTextResult,
            await self._command("setContainerQueryText", params, session_id, kwargs),
        )

    @overload
    async def setContainerQueryConditionText(
        self,
        params: SetContainerQueryConditionTextParameters,
        session_id: str | None = None,
    ) -> SetContainerQueryConditionTextResult: ...

    @overload
    async def setContainerQueryConditionText(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetContainerQueryConditionTextParameters],
    ) -> SetContainerQueryConditionTextResult: ...

    async def setContainerQueryConditionText(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> SetContainerQueryConditionTextResult:
        """Send CSS.setContainerQueryConditionText."""

        return cast(
            SetContainerQueryConditionTextResult,
            await self._command(
                "setContainerQueryConditionText", params, session_id, kwargs
            ),
        )

    @overload
    async def setSupportsText(
        self,
        params: SetSupportsTextParameters,
        session_id: str | None = None,
    ) -> SetSupportsTextResult: ...

    @overload
    async def setSupportsText(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetSupportsTextParameters],
    ) -> SetSupportsTextResult: ...

    async def setSupportsText(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> SetSupportsTextResult:
        """Modifies the expression of a supports at-rule."""

        return cast(
            SetSupportsTextResult,
            await self._command("setSupportsText", params, session_id, kwargs),
        )

    @overload
    async def setNavigationText(
        self,
        params: SetNavigationTextParameters,
        session_id: str | None = None,
    ) -> SetNavigationTextResult: ...

    @overload
    async def setNavigationText(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetNavigationTextParameters],
    ) -> SetNavigationTextResult: ...

    async def setNavigationText(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> SetNavigationTextResult:
        """Modifies the expression of a navigation at-rule."""

        return cast(
            SetNavigationTextResult,
            await self._command("setNavigationText", params, session_id, kwargs),
        )

    @overload
    async def setScopeText(
        self,
        params: SetScopeTextParameters,
        session_id: str | None = None,
    ) -> SetScopeTextResult: ...

    @overload
    async def setScopeText(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetScopeTextParameters],
    ) -> SetScopeTextResult: ...

    async def setScopeText(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> SetScopeTextResult:
        """Modifies the expression of a scope at-rule."""

        return cast(
            SetScopeTextResult,
            await self._command("setScopeText", params, session_id, kwargs),
        )

    @overload
    async def setRuleSelector(
        self,
        params: SetRuleSelectorParameters,
        session_id: str | None = None,
    ) -> SetRuleSelectorResult: ...

    @overload
    async def setRuleSelector(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetRuleSelectorParameters],
    ) -> SetRuleSelectorResult: ...

    async def setRuleSelector(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> SetRuleSelectorResult:
        """Modifies the rule selector."""

        return cast(
            SetRuleSelectorResult,
            await self._command("setRuleSelector", params, session_id, kwargs),
        )

    @overload
    async def setStyleSheetText(
        self,
        params: SetStyleSheetTextParameters,
        session_id: str | None = None,
    ) -> SetStyleSheetTextResult: ...

    @overload
    async def setStyleSheetText(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetStyleSheetTextParameters],
    ) -> SetStyleSheetTextResult: ...

    async def setStyleSheetText(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> SetStyleSheetTextResult:
        """Sets the new stylesheet text."""

        return cast(
            SetStyleSheetTextResult,
            await self._command("setStyleSheetText", params, session_id, kwargs),
        )

    @overload
    async def setStyleTexts(
        self,
        params: SetStyleTextsParameters,
        session_id: str | None = None,
    ) -> SetStyleTextsResult: ...

    @overload
    async def setStyleTexts(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetStyleTextsParameters],
    ) -> SetStyleTextsResult: ...

    async def setStyleTexts(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> SetStyleTextsResult:
        """Applies specified style edits one after another in the given order."""

        return cast(
            SetStyleTextsResult,
            await self._command("setStyleTexts", params, session_id, kwargs),
        )

    async def startRuleUsageTracking(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Enables the selector recording."""

        return await self._command("startRuleUsageTracking", None, session_id, {})

    async def stopRuleUsageTracking(
        self,
        session_id: str | None = None,
    ) -> StopRuleUsageTrackingResult:
        """Stop tracking rule usage and return the list of rules that were used since last call to `takeCoverageDelta` (or since start of coverage instrumentation)."""

        return cast(
            StopRuleUsageTrackingResult,
            await self._command("stopRuleUsageTracking", None, session_id, {}),
        )

    async def takeCoverageDelta(
        self,
        session_id: str | None = None,
    ) -> TakeCoverageDeltaResult:
        """Obtain list of rules that became used since last call to this method (or since start of coverage instrumentation)."""

        return cast(
            TakeCoverageDeltaResult,
            await self._command("takeCoverageDelta", None, session_id, {}),
        )

    @overload
    async def setLocalFontsEnabled(
        self,
        params: SetLocalFontsEnabledParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def setLocalFontsEnabled(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[SetLocalFontsEnabledParameters],
    ) -> JsonObject: ...

    async def setLocalFontsEnabled(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Enables/disables rendering of local CSS fonts (enabled by default)."""

        return await self._command("setLocalFontsEnabled", params, session_id, kwargs)

    @overload
    def fontsUpdated(
        self,
        callback_or_session: EventCallback[FontsUpdatedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def fontsUpdated(
        self,
        callback_or_session: str,
        handler: EventCallback[FontsUpdatedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def fontsUpdated(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[FontsUpdatedEvent]: ...

    def fontsUpdated(
        self,
        callback_or_session: EventCallback[FontsUpdatedEvent] | str | None = None,
        handler: EventCallback[FontsUpdatedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[FontsUpdatedEvent] | Unsubscribe:
        """Fires whenever a web font is updated. A non-empty font parameter indicates a successfully loaded web font."""

        return cast(
            Awaitable[FontsUpdatedEvent] | Unsubscribe,
            self._event(
                "fontsUpdated",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def mediaQueryResultChanged(
        self,
        callback_or_session: EventCallback[JsonObject],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def mediaQueryResultChanged(
        self,
        callback_or_session: str,
        handler: EventCallback[JsonObject],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def mediaQueryResultChanged(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[JsonObject]: ...

    def mediaQueryResultChanged(
        self,
        callback_or_session: EventCallback[JsonObject] | str | None = None,
        handler: EventCallback[JsonObject] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[JsonObject] | Unsubscribe:
        """Fires whenever a MediaQuery result changes (for example, after a browser window has been resized.) The current implementation considers only viewport-dependent media features."""

        return self._event(
            "mediaQueryResultChanged",
            cast(EventCallback[Mapping[str, object]] | str | None, callback_or_session),
            cast(EventCallback[Mapping[str, object]] | None, handler),
            session_id,
        )

    @overload
    def styleSheetAdded(
        self,
        callback_or_session: EventCallback[StyleSheetAddedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def styleSheetAdded(
        self,
        callback_or_session: str,
        handler: EventCallback[StyleSheetAddedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def styleSheetAdded(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[StyleSheetAddedEvent]: ...

    def styleSheetAdded(
        self,
        callback_or_session: EventCallback[StyleSheetAddedEvent] | str | None = None,
        handler: EventCallback[StyleSheetAddedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[StyleSheetAddedEvent] | Unsubscribe:
        """Fired whenever an active document stylesheet is added."""

        return cast(
            Awaitable[StyleSheetAddedEvent] | Unsubscribe,
            self._event(
                "styleSheetAdded",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def styleSheetChanged(
        self,
        callback_or_session: EventCallback[StyleSheetChangedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def styleSheetChanged(
        self,
        callback_or_session: str,
        handler: EventCallback[StyleSheetChangedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def styleSheetChanged(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[StyleSheetChangedEvent]: ...

    def styleSheetChanged(
        self,
        callback_or_session: EventCallback[StyleSheetChangedEvent] | str | None = None,
        handler: EventCallback[StyleSheetChangedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[StyleSheetChangedEvent] | Unsubscribe:
        """Fired whenever a stylesheet is changed as a result of the client operation."""

        return cast(
            Awaitable[StyleSheetChangedEvent] | Unsubscribe,
            self._event(
                "styleSheetChanged",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def styleSheetRemoved(
        self,
        callback_or_session: EventCallback[StyleSheetRemovedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def styleSheetRemoved(
        self,
        callback_or_session: str,
        handler: EventCallback[StyleSheetRemovedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def styleSheetRemoved(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[StyleSheetRemovedEvent]: ...

    def styleSheetRemoved(
        self,
        callback_or_session: EventCallback[StyleSheetRemovedEvent] | str | None = None,
        handler: EventCallback[StyleSheetRemovedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[StyleSheetRemovedEvent] | Unsubscribe:
        """Fired whenever an active document stylesheet is removed."""

        return cast(
            Awaitable[StyleSheetRemovedEvent] | Unsubscribe,
            self._event(
                "styleSheetRemoved",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def computedStyleUpdated(
        self,
        callback_or_session: EventCallback[ComputedStyleUpdatedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def computedStyleUpdated(
        self,
        callback_or_session: str,
        handler: EventCallback[ComputedStyleUpdatedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def computedStyleUpdated(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ComputedStyleUpdatedEvent]: ...

    def computedStyleUpdated(
        self,
        callback_or_session: EventCallback[ComputedStyleUpdatedEvent]
        | str
        | None = None,
        handler: EventCallback[ComputedStyleUpdatedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[ComputedStyleUpdatedEvent] | Unsubscribe:
        """Wait for or subscribe to CSS.computedStyleUpdated."""

        return cast(
            Awaitable[ComputedStyleUpdatedEvent] | Unsubscribe,
            self._event(
                "computedStyleUpdated",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )


__all__ = [
    "CSS",
    "AddRuleParameters",
    "AddRuleResult",
    "CSSAnimationStyle",
    "CSSAtRule",
    "CSSComputedStyleProperty",
    "CSSContainerQuery",
    "CSSFunctionConditionNode",
    "CSSFunctionNode",
    "CSSFunctionParameter",
    "CSSFunctionRule",
    "CSSKeyframeRule",
    "CSSKeyframesRule",
    "CSSLayer",
    "CSSLayerData",
    "CSSMedia",
    "CSSNavigation",
    "CSSPositionTryRule",
    "CSSProperty",
    "CSSPropertyRegistration",
    "CSSPropertyRule",
    "CSSRule",
    "CSSRuleType",
    "CSSScope",
    "CSSStartingStyle",
    "CSSStyle",
    "CSSStyleSheetHeader",
    "CSSSupports",
    "CSSTryRule",
    "CollectClassNamesParameters",
    "CollectClassNamesResult",
    "ComputedStyleExtraFields",
    "ComputedStyleUpdatedEvent",
    "CreateStyleSheetParameters",
    "CreateStyleSheetResult",
    "FontFace",
    "FontVariationAxis",
    "FontsUpdatedEvent",
    "ForcePseudoStateParameters",
    "ForceStartingStyleParameters",
    "GetAnimatedStylesForNodeParameters",
    "GetAnimatedStylesForNodeResult",
    "GetBackgroundColorsParameters",
    "GetBackgroundColorsResult",
    "GetComputedStyleForNodeParameters",
    "GetComputedStyleForNodeResult",
    "GetEnvironmentVariablesResult",
    "GetInlineStylesForNodeParameters",
    "GetInlineStylesForNodeResult",
    "GetLayersForNodeParameters",
    "GetLayersForNodeResult",
    "GetLocationForSelectorParameters",
    "GetLocationForSelectorResult",
    "GetLonghandPropertiesParameters",
    "GetLonghandPropertiesResult",
    "GetMatchedStylesForNodeParameters",
    "GetMatchedStylesForNodeResult",
    "GetMediaQueriesResult",
    "GetPlatformFontsForNodeParameters",
    "GetPlatformFontsForNodeResult",
    "GetStyleSheetTextParameters",
    "GetStyleSheetTextResult",
    "InheritedAnimatedStyleEntry",
    "InheritedPseudoElementMatches",
    "InheritedStyleEntry",
    "MediaQuery",
    "MediaQueryExpression",
    "PlatformFontUsage",
    "PseudoElementMatches",
    "ResolveValuesParameters",
    "ResolveValuesResult",
    "RuleMatch",
    "RuleUsage",
    "SelectorList",
    "SetContainerQueryConditionTextParameters",
    "SetContainerQueryConditionTextResult",
    "SetContainerQueryTextParameters",
    "SetContainerQueryTextResult",
    "SetEffectivePropertyValueForNodeParameters",
    "SetKeyframeKeyParameters",
    "SetKeyframeKeyResult",
    "SetLocalFontsEnabledParameters",
    "SetMediaTextParameters",
    "SetMediaTextResult",
    "SetNavigationTextParameters",
    "SetNavigationTextResult",
    "SetPropertyRulePropertyNameParameters",
    "SetPropertyRulePropertyNameResult",
    "SetRuleSelectorParameters",
    "SetRuleSelectorResult",
    "SetScopeTextParameters",
    "SetScopeTextResult",
    "SetStyleSheetTextParameters",
    "SetStyleSheetTextResult",
    "SetStyleTextsParameters",
    "SetStyleTextsResult",
    "SetSupportsTextParameters",
    "SetSupportsTextResult",
    "ShorthandEntry",
    "SourceRange",
    "Specificity",
    "SpecificityComponent",
    "StopRuleUsageTrackingResult",
    "StyleDeclarationEdit",
    "StyleSheetAddedEvent",
    "StyleSheetChangedEvent",
    "StyleSheetOrigin",
    "StyleSheetRemovedEvent",
    "TakeComputedStyleUpdatesResult",
    "TakeCoverageDeltaResult",
    "TrackComputedStyleUpdatesForNodeParameters",
    "TrackComputedStyleUpdatesParameters",
    "Value",
]
