import asyncio
from types import SimpleNamespace
from typing import Any, Callable

from google.genai.client import AsyncClient
from neispy import Neispy
from sanic.app import Sanic
from sanic.request import Request
from valkey.asyncio import Valkey

from backend.infrastructure.config import BackendConfig
from backend.infrastructure.genai.repositories.calorie import GeminiCalorieRepository
from backend.infrastructure.neispy.repositories.meal import NeispyMealRepository
from backend.infrastructure.neispy.repositories.school import NeispySchoolRepository
from backend.infrastructure.neispy.repositories.timetable import NeispyTimetableRepository
from backend.infrastructure.sqlalchemy import SQLAlchemy
from backend.infrastructure.sqlalchemy.repositories.comment import (
    SQLAlchemyCommentRepository,
)
from backend.infrastructure.sqlalchemy.repositories.meal import SQLAlchemyMealRepository
from backend.infrastructure.sqlalchemy.repositories.rating import SQLAlchemyRatingRepository
from backend.infrastructure.sqlalchemy.repositories.school_info import SQLAlchemySchoolInfoRepository
from backend.infrastructure.sqlalchemy.repositories.user import SQLAlchemyUserRepository
from backend.infrastructure.sqlalchemy.repositories.timetable import (
    SQLAlchemyTimetableRepository,
)
from backend.infrastructure.valkey.entities.repositories.refresh_token import (
    ValkeyRefreshTokenRepository,
)


class BackendContext(SimpleNamespace):
    sa: SQLAlchemy
    valkey: Valkey
    neispy: Neispy
    gemini: AsyncClient
    user_repository: SQLAlchemyUserRepository
    comment_repository: SQLAlchemyCommentRepository
    timetable_repository: SQLAlchemyTimetableRepository
    refresh_token_repository: ValkeyRefreshTokenRepository
    neispy_school_repository: NeispySchoolRepository
    neispy_meal_repository: NeispyMealRepository
    neispy_timetable_repository: NeispyTimetableRepository
    sa_meal_repository: SQLAlchemyMealRepository
    calorie_repository: GeminiCalorieRepository
    school_info_repository: SQLAlchemySchoolInfoRepository
    rating_repository: SQLAlchemyRatingRepository
    jwt_encode: Callable[[dict[str, Any]], str]
    jwt_decode: Callable[[str], dict[str, Any]]
    lock: asyncio.Lock


class Backend(Sanic[BackendConfig, BackendContext]):
    ctx: BackendContext


class BackendRequest(Request):
    app: Backend
