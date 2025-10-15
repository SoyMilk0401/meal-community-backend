from sanic.blueprints import Blueprint

from backend.adapters.controllers.endpoint.api.comment import comment
from backend.adapters.controllers.endpoint.api.meal import meal
from backend.adapters.controllers.endpoint.api.school import school
from backend.adapters.controllers.endpoint.api.user import user
from backend.adapters.controllers.endpoint.api.calorie import calorie
from backend.adapters.controllers.endpoint.api.timetable import timetable
from backend.adapters.controllers.endpoint.api.rating import rating

api_endpoint = Blueprint.group(
    user,
    school,
    meal,
    comment,
    calorie,
    timetable,
    rating,
    url_prefix="/api",
)
