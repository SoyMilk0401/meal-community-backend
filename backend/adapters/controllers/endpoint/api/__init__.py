from sanic.blueprints import Blueprint

from backend.adapters.controllers.endpoint.api.user import user
from backend.adapters.controllers.endpoint.api.school import school

api_endpoint = Blueprint.group(
    user,
    school,
    url_prefix="/api",
)
