from types import SimpleNamespace
from typing import Any, Callable


from sanic.app import Sanic
from sanic.request import Request
from valkey.asyncio import Valkey

from backend.infrastructure.config import BackendConfig
from backend.infrastructure.sqlalchemy import SQLAlchemy
from backend.infrastructure.valkey.entities.repositories.refresh_token import (
    ValkeyRefreshTokenRepository,
)
from backend.infrastructure.sqlalchemy.repositories.user import SQLAlchemyUserRepository


class BackendContext(SimpleNamespace):
    sa: SQLAlchemy
    valkey: Valkey
    user_repository: SQLAlchemyUserRepository
    refresh_token_repository: ValkeyRefreshTokenRepository
    jwt_encode: Callable[[dict[str, Any]], str]
    jwt_decode: Callable[[str], dict[str, Any]]


class Backend(Sanic[BackendConfig, BackendContext]):
    ctx: BackendContext


class BackendRequest(Request):
    app: Backend
