from types import SimpleNamespace


from sanic.app import Sanic
from sanic.request import Request

from backend.infrastructure.config import BackendConfig
from backend.infrastructure.sqlalchemy. import SQLAlchemy
from backend.infrastructure.sqlalchemy.repository.user import SQLAlchemyUserRepository


class BackendContext(SimpleNamespace):
    sa: SQLAlchemy
    user_repository: SQLAlchemyUserRepository


class Backend(Sanic[BackendConfig, BackendContext]):
    ctx: BackendContext


class BackendRequest(Request):
    app: Backend
