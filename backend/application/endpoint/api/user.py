from sanic.blueprints import Blueprint

from backend.application.sanic import BackendRequest

user = Blueprint("user_endpoint", url_prefix="/user")


@user.post("/register")
async def register_user(request: BackendRequest): ...


@user.get("/login")
async def login_user(request: BackendRequest): ...


@user.get("/logout")
async def logout_user(request: BackendRequest): ...


@user.get("/me")
async def get_user(request: BackendRequest): ...


@user.post("/modify")
async def modify_user(request: BackendRequest): ...
