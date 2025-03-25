from sanic.blueprints import Blueprint

from backend.application.endpoint.api.user import user_endpoint

api_endpoint = Blueprint.group(
    user_endpoint,
    url_prefix="/api",
)
