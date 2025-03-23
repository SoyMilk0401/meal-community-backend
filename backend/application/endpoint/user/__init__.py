from sanic.blueprints import Blueprint


user_endpoint = Blueprint.group(
    url_prefix="/user",
)
