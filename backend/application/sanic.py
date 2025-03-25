from types import SimpleNamespace


from sanic.app import Sanic
from sanic.request import Request

from backend.application.config import BackendConfig
from backend.infrastructure.sqlalchemy import SQLAlchemy


class BackendContext(SimpleNamespace):
    sa: SQLAlchemy


class Backend(Sanic[BackendConfig, BackendContext]):
    ctx: BackendContext


class BackendRequest(Request):
    app: Backend
