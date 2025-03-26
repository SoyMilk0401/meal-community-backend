from dataclasses import asdict
from sanic import BadRequest, json
from sanic.blueprints import Blueprint
from sanic_ext import validate
from sanic_jwt import protected  # type: ignore
from backend.infrastructure.sanic import BackendRequest
from backend.domain.entities.user import User
from backend.application.use_cases.create.user import CreateUserUseCase
from backend.application.use_cases.get.user import GetByEmailWithPasswordUserUseCase

user = Blueprint("user_endpoint", url_prefix="/user")


@user.post("/register")
@validate(json=User, body_argument="user")
async def register_user(
    request: BackendRequest,
    user: User,
):
    a = await CreateUserUseCase(request.app.ctx.user_repository).execute(user)
    return json(asdict(a))


async def login_user(request: BackendRequest):
    email = request.json.get("email")
    password = request.json.get("password")

    if not email or not password:
        raise BadRequest("email or password is missing")

    user = await GetByEmailWithPasswordUserUseCase(
        request.app.ctx.user_repository
    ).execute(email, password)

    return json(asdict(user))


@user.get("/logout")
async def logout_user(request: BackendRequest): ...


@user.get("/me")
async def get_user(request: BackendRequest): ...


@user.post("/modify")
async def modify_user(request: BackendRequest): ...
