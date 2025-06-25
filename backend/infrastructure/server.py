import asyncio
from asyncio import AbstractEventLoop
from functools import partial

from google.genai import Client
from neispy import Neispy
from valkey.asyncio import Valkey

from backend.adapters.controllers.endpoint import endpoint
from backend.infrastructure.config import BackendConfig
from backend.infrastructure.error import ErrorHandler
from backend.infrastructure.genai.repositories.calorie import GeminiCalorieRepository
from backend.infrastructure.jwt import jwt_decode, jwt_encode
from backend.infrastructure.neispy.repositories.meal import NeispyMealRepository
from backend.infrastructure.neispy.repositories.school import NeispySchoolRepository
from backend.infrastructure.sanic import Backend
from backend.infrastructure.sqlalchemy import SQLAlchemy
from backend.infrastructure.sqlalchemy.repositories.comment import (
    SQLAlchemyCommentRepository,
)
from backend.infrastructure.sqlalchemy.repositories.meal import SQLAlchemyMealRepository
from backend.infrastructure.sqlalchemy.repositories.user import SQLAlchemyUserRepository
from backend.infrastructure.valkey.entities.repositories.refresh_token import (
    ValkeyRefreshTokenRepository,
)


async def startup(app: Backend, loop: AbstractEventLoop) -> None:
    # Initialize Infrastructure Components
    app.ctx.sa = await SQLAlchemy.create(app.config.DB_URL)
    app.ctx.valkey = Valkey.from_url(app.config.VALKEY_URL)
    app.ctx.neispy = Neispy(app.config.NEIS_API_KEY)
    app.ctx.gemini = Client(api_key=app.config.GEMINI_API_KEY).aio

    # Initialize Repositories
    app.ctx.user_repository = SQLAlchemyUserRepository(app.ctx.sa)
    app.ctx.comment_repository = SQLAlchemyCommentRepository(app.ctx.sa)
    app.ctx.refresh_token_repository = ValkeyRefreshTokenRepository(
        app.ctx.valkey, app.config.REFRESH_TOKEN_EXP
    )
    app.ctx.neispy_school_repository = NeispySchoolRepository(app.ctx.neispy)
    app.ctx.neispy_meal_repository = NeispyMealRepository(app.ctx.neispy)
    app.ctx.sa_meal_repository = SQLAlchemyMealRepository(app.ctx.sa)
    app.ctx.calorie_repository = GeminiCalorieRepository(app.ctx.gemini)

    # Initialize External Services
    app.ctx.jwt_encode = partial(
        jwt_encode, secret=app.config.JWT_SECRET, exp=app.config.ACCESS_TOKEN_EXP
    )
    app.ctx.jwt_decode = partial(jwt_decode, secret=app.config.JWT_SECRET)
    app.ctx.lock = asyncio.Lock()


async def closeup(app: Backend, loop: AbstractEventLoop) -> None:
    await app.ctx.sa.engine.dispose()


def create_app(config: BackendConfig) -> Backend:
    backend = Backend("backend", error_handler=ErrorHandler())
    backend.static("/", "/frontend/index.html", name="index")
    backend.static("/assets", "/frontend/assets", name="static")
    backend.static("/meal.png", "/frontend/meal.png", name="main_image")
    backend.static("/vite.svf", "/frontend/vite.svg", name="favicon")
    config.CORS_ORIGINS = "https://meal.solo.moe"
    config.CORS_SUPPORTS_CREDENTIALS = True
    config.CORS_ALLOW_HEADERS = ["Content-Type", "Authorization", "Set-Cookie"]
    backend.config.update(config)
    backend.blueprint(endpoint)
    backend.before_server_start(startup)
    backend.before_server_stop(closeup)

    return backend
