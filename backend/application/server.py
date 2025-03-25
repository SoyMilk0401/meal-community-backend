from asyncio import AbstractEventLoop

from backend.application.config import BackendConfig
from backend.application.endpoint import endpoint
from backend.application.sanic import Backend
from backend.infrastructure.sqlalchemy import SQLAlchemy


async def startup(app: Backend, loop: AbstractEventLoop) -> None:
    app.ctx.sa = await SQLAlchemy.create(app.config.DB_URL)


async def closeup(app: Backend, loop: AbstractEventLoop) -> None:
    await app.ctx.sa.engine.dispose()


def create_app(config: BackendConfig) -> Backend:
    backend = Backend("backend")
    backend.config.update(config)
    backend.blueprint(endpoint)
    backend.before_server_start(startup)
    backend.before_server_stop(closeup)

    return backend
