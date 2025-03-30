from types import SimpleNamespace
from sanic import Config, Request, Sanic
from sanic.handlers import ErrorHandler as SanicErrorHandler
from sanic.response.types import HTTPResponse
from backend.application.exceptions import *
from sanic import json


class ErrorHandler(SanicErrorHandler):
    def default(
        self,
        request: Request[Sanic[Config, SimpleNamespace], SimpleNamespace],
        exception: Exception,
    ) -> HTTPResponse:
        if isinstance(exception, BackendException):
            return json(
                {
                    "message": str(exception),
                },
                status=exception.code,
            )

        return super().default(request, exception)
