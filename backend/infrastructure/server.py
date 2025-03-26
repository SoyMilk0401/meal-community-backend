from asyncio import AbstractEventLoop


from backend.infrastructure.config import BackendConfig
from backend.adapters.controllers.endpoint import endpoint
from backend.infrastructure.sanic import Backend

from backend.infrastructure.sqlalchemy import SQLAlchemy
from backend.infrastructure.sqlalchemy.repository.user import SQLAlchemyUserRepository

from sanic_jwt import Initialize


async def startup(app: Backend, loop: AbstractEventLoop) -> None:
    app.ctx.sa = await SQLAlchemy.create(app.config.DB_URL)
    app.ctx.user_repository = SQLAlchemyUserRepository(app.ctx.sa)


async def closeup(app: Backend, loop: AbstractEventLoop) -> None:
    await app.ctx.sa.engine.dispose()


def create_app(config: BackendConfig) -> Backend:
    backend = Backend("backend")
    Initialize(backend)
    backend.config.update(config)
    backend.blueprint(endpoint)
    backend.before_server_start(startup)
    backend.before_server_stop(closeup)

    return backend
