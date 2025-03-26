from sanic.blueprints import Blueprint

from backend.adapters.controllers.endpoint.api.user import user

api_endpoint = Blueprint.group(
    user,
    url_prefix="/api",
)
