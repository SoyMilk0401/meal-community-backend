from sanic.blueprints import Blueprint

from backend.adapters.controllers.endpoint.api.user import user
from backend.adapters.controllers.endpoint.api.school import school
from backend.adapters.controllers.endpoint.api.meal import meal

api_endpoint = Blueprint.group(
    user,
    school,
    meal,
    url_prefix="/api",
)
