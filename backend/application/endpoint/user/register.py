from sanic.blueprints import Blueprint

register = Blueprint("user_register", url_prefix="/register")


@register.post("/")
async def register_user(request): ...
