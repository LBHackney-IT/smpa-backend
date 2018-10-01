from typing import Any, Callable, Optional
from molten import HTTP_403, HTTPError, Header, Request
from ..helpers.console import console


def AuthorizationMiddleware(handler: Callable[..., Any]) -> Callable[..., Any]:

    def middleware(request: Request, authorization: Optional[Header]) -> Any:
        no_auth = ["/_docs", "/_schema", "/_debugger"]

        if authorization != "Bearer secret" and request.path not in no_auth:
            raise HTTPError(HTTP_403, {"error": "forbidden"})
        return handler()

    return middleware
