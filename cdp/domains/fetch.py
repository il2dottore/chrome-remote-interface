"""Generated bindings for the CDP Fetch domain. Do not edit manually."""

from __future__ import annotations

from collections.abc import Awaitable, Mapping
from typing import TYPE_CHECKING, Literal, TypeAlias, cast, overload

from typing_extensions import NotRequired, TypedDict, Unpack

from cdp.domain import Domain as BaseDomain, EventCallback, Unsubscribe
from cdp.types import JsonObject

if TYPE_CHECKING:
    from . import io as IO
    from . import network as Network
    from . import page as Page


RequestId: TypeAlias = str

RequestStage: TypeAlias = Literal["Request", "Response"]


class RequestPattern(TypedDict):
    urlPattern: NotRequired[str]
    resourceType: NotRequired[Network.ResourceType]
    requestStage: NotRequired[RequestStage]


class HeaderEntry(TypedDict):
    name: str
    value: str


class AuthChallenge(TypedDict):
    source: NotRequired[Literal["Server", "Proxy"]]
    origin: str
    scheme: str
    realm: str


class AuthChallengeResponse(TypedDict):
    response: Literal["Default", "CancelAuth", "ProvideCredentials"]
    username: NotRequired[str]
    password: NotRequired[str]


class EnableParameters(TypedDict):
    patterns: NotRequired[list[RequestPattern]]
    handleAuthRequests: NotRequired[bool]


class FailRequestParameters(TypedDict):
    requestId: RequestId
    errorReason: Network.ErrorReason


class FulfillRequestParameters(TypedDict):
    requestId: RequestId
    responseCode: int
    responseHeaders: NotRequired[list[HeaderEntry]]
    binaryResponseHeaders: NotRequired[str]
    body: NotRequired[str]
    responsePhrase: NotRequired[str]


class ContinueRequestParameters(TypedDict):
    requestId: RequestId
    url: NotRequired[str]
    method: NotRequired[str]
    postData: NotRequired[str]
    headers: NotRequired[list[HeaderEntry]]
    interceptResponse: NotRequired[bool]


class ContinueWithAuthParameters(TypedDict):
    requestId: RequestId
    authChallengeResponse: AuthChallengeResponse


class ContinueResponseParameters(TypedDict):
    requestId: RequestId
    responseCode: NotRequired[int]
    responsePhrase: NotRequired[str]
    responseHeaders: NotRequired[list[HeaderEntry]]
    binaryResponseHeaders: NotRequired[str]


class GetResponseBodyParameters(TypedDict):
    requestId: RequestId


class GetResponseBodyResult(TypedDict):
    body: str
    base64Encoded: bool


class TakeResponseBodyAsStreamParameters(TypedDict):
    requestId: RequestId


class TakeResponseBodyAsStreamResult(TypedDict):
    stream: IO.StreamHandle


class RequestPausedEvent(TypedDict):
    requestId: RequestId
    request: Network.Request
    frameId: Page.FrameId
    resourceType: Network.ResourceType
    responseErrorReason: NotRequired[Network.ErrorReason]
    responseStatusCode: NotRequired[int]
    responseStatusText: NotRequired[str]
    responseHeaders: NotRequired[list[HeaderEntry]]
    networkId: NotRequired[Network.RequestId]
    redirectedRequestId: NotRequired[RequestId]


class AuthRequiredEvent(TypedDict):
    requestId: RequestId
    request: Network.Request
    frameId: Page.FrameId
    resourceType: Network.ResourceType
    authChallenge: AuthChallenge


class Fetch(BaseDomain):
    """A domain for letting clients substitute browser's network layer with client code."""

    domain_name = "Fetch"

    async def disable(
        self,
        session_id: str | None = None,
    ) -> JsonObject:
        """Disables the fetch domain."""

        return await self._command("disable", None, session_id, {})

    @overload
    async def enable(
        self,
        params: EnableParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def enable(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[EnableParameters],
    ) -> JsonObject: ...

    async def enable(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Enables issuing of requestPaused events. A request will be paused until client calls one of failRequest, fulfillRequest or continueRequest/continueWithAuth."""

        return await self._command("enable", params, session_id, kwargs)

    @overload
    async def failRequest(
        self,
        params: FailRequestParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def failRequest(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[FailRequestParameters],
    ) -> JsonObject: ...

    async def failRequest(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Causes the request to fail with specified reason."""

        return await self._command("failRequest", params, session_id, kwargs)

    @overload
    async def fulfillRequest(
        self,
        params: FulfillRequestParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def fulfillRequest(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[FulfillRequestParameters],
    ) -> JsonObject: ...

    async def fulfillRequest(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Provides response to the request."""

        return await self._command("fulfillRequest", params, session_id, kwargs)

    @overload
    async def continueRequest(
        self,
        params: ContinueRequestParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def continueRequest(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[ContinueRequestParameters],
    ) -> JsonObject: ...

    async def continueRequest(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Continues the request, optionally modifying some of its parameters."""

        return await self._command("continueRequest", params, session_id, kwargs)

    @overload
    async def continueWithAuth(
        self,
        params: ContinueWithAuthParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def continueWithAuth(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[ContinueWithAuthParameters],
    ) -> JsonObject: ...

    async def continueWithAuth(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Continues a request supplying authChallengeResponse following authRequired event."""

        return await self._command("continueWithAuth", params, session_id, kwargs)

    @overload
    async def continueResponse(
        self,
        params: ContinueResponseParameters,
        session_id: str | None = None,
    ) -> JsonObject: ...

    @overload
    async def continueResponse(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[ContinueResponseParameters],
    ) -> JsonObject: ...

    async def continueResponse(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> JsonObject:
        """Continues loading of the paused response, optionally modifying the response headers. If either responseCode or headers are modified, all of them must be present."""

        return await self._command("continueResponse", params, session_id, kwargs)

    @overload
    async def getResponseBody(
        self,
        params: GetResponseBodyParameters,
        session_id: str | None = None,
    ) -> GetResponseBodyResult: ...

    @overload
    async def getResponseBody(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[GetResponseBodyParameters],
    ) -> GetResponseBodyResult: ...

    async def getResponseBody(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> GetResponseBodyResult:
        """Causes the body of the response to be received from the server and returned as a single string. May only be issued for a request that is paused in the Response stage and is mutually exclusive with takeResponseBodyForInterceptionAsStream. Calling other methods that affect the request or disabling fetch domain before body is received results in an undefined behavior. Note that the response body is not available for redirects. Requests paused in the _redirect received_ state may be differentiated by `responseCode` and presence of `location` response header, see comments to `requestPaused` for details."""

        return cast(
            GetResponseBodyResult,
            await self._command("getResponseBody", params, session_id, kwargs),
        )

    @overload
    async def takeResponseBodyAsStream(
        self,
        params: TakeResponseBodyAsStreamParameters,
        session_id: str | None = None,
    ) -> TakeResponseBodyAsStreamResult: ...

    @overload
    async def takeResponseBodyAsStream(
        self,
        params: str | None = None,
        session_id: str | None = None,
        **kwargs: Unpack[TakeResponseBodyAsStreamParameters],
    ) -> TakeResponseBodyAsStreamResult: ...

    async def takeResponseBodyAsStream(
        self,
        params: Mapping[str, object] | str | None = None,
        session_id: str | None = None,
        **kwargs: object,
    ) -> TakeResponseBodyAsStreamResult:
        """Returns a handle to the stream representing the response body. The request must be paused in the HeadersReceived stage. Note that after this command the request can't be continued as is -- client either needs to cancel it or to provide the response body. The stream only supports sequential read, IO.read will fail if the position is specified. This method is mutually exclusive with getResponseBody. Calling other methods that affect the request or disabling fetch domain before body is received results in an undefined behavior."""

        return cast(
            TakeResponseBodyAsStreamResult,
            await self._command("takeResponseBodyAsStream", params, session_id, kwargs),
        )

    @overload
    def requestPaused(
        self,
        callback_or_session: EventCallback[RequestPausedEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def requestPaused(
        self,
        callback_or_session: str,
        handler: EventCallback[RequestPausedEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def requestPaused(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[RequestPausedEvent]: ...

    def requestPaused(
        self,
        callback_or_session: EventCallback[RequestPausedEvent] | str | None = None,
        handler: EventCallback[RequestPausedEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[RequestPausedEvent] | Unsubscribe:
        """Issued when the domain is enabled and the request URL matches the specified filter. The request is paused until the client responds with one of continueRequest, failRequest or fulfillRequest. The stage of the request can be determined by presence of responseErrorReason and responseStatusCode -- the request is at the response stage if either of these fields is present and in the request stage otherwise. Redirect responses and subsequent requests are reported similarly to regular responses and requests. Redirect responses may be distinguished by the value of `responseStatusCode` (which is one of 301, 302, 303, 307, 308) along with presence of the `location` header. Requests resulting from a redirect will have `redirectedRequestId` field set."""

        return cast(
            Awaitable[RequestPausedEvent] | Unsubscribe,
            self._event(
                "requestPaused",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )

    @overload
    def authRequired(
        self,
        callback_or_session: EventCallback[AuthRequiredEvent],
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def authRequired(
        self,
        callback_or_session: str,
        handler: EventCallback[AuthRequiredEvent],
        *,
        session_id: str | None = None,
    ) -> Unsubscribe: ...

    @overload
    def authRequired(
        self,
        callback_or_session: str | None = None,
        handler: None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[AuthRequiredEvent]: ...

    def authRequired(
        self,
        callback_or_session: EventCallback[AuthRequiredEvent] | str | None = None,
        handler: EventCallback[AuthRequiredEvent] | None = None,
        *,
        session_id: str | None = None,
    ) -> Awaitable[AuthRequiredEvent] | Unsubscribe:
        """Issued when the domain is enabled with handleAuthRequests set to true. The request is paused until client responds with continueWithAuth."""

        return cast(
            Awaitable[AuthRequiredEvent] | Unsubscribe,
            self._event(
                "authRequired",
                cast(
                    EventCallback[Mapping[str, object]] | str | None,
                    callback_or_session,
                ),
                cast(EventCallback[Mapping[str, object]] | None, handler),
                session_id,
            ),
        )


__all__ = [
    "AuthChallenge",
    "AuthChallengeResponse",
    "AuthRequiredEvent",
    "ContinueRequestParameters",
    "ContinueResponseParameters",
    "ContinueWithAuthParameters",
    "EnableParameters",
    "FailRequestParameters",
    "Fetch",
    "FulfillRequestParameters",
    "GetResponseBodyParameters",
    "GetResponseBodyResult",
    "HeaderEntry",
    "RequestId",
    "RequestPattern",
    "RequestPausedEvent",
    "RequestStage",
    "TakeResponseBodyAsStreamParameters",
    "TakeResponseBodyAsStreamResult",
]
