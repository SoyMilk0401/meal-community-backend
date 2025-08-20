from io import BytesIO

from sanic import json
from sanic.blueprints import Blueprint
from sanic_ext import openapi
from sanic_ext.extensions.openapi.types import Binary, Integer

from backend.application.use_cases.get.calorie import GetCalorieUseCase
from backend.application.use_cases.get.meal import GetDailyMealByIDUseCase
from backend.infrastructure.jwt import require_auth
from backend.infrastructure.sanic import BackendRequest

calorie = Blueprint("calorie_endpoint", url_prefix="/calorie")


@openapi.body(
    {"multipart/form-data": {"file": Binary(), "meal_id": Integer()}}, required=True
)
@calorie.post("/inference")
@require_auth
async def get_calories_by_meal_image(
    request: BackendRequest,
    _,
):
    if not request.form:
        return json({"error": "Form data is required"}, status=400)

    meal_id = request.form.get("meal_id")

    if not meal_id:
        return json({"error": "Meal ID is required"}, status=400)

    meal = await GetDailyMealByIDUseCase(request.app.ctx.sa_meal_repository).execute(
        meal_id
    )

    if not request.files:
        return json({"error": "Image file is required"}, status=400)

    image = request.files.get("image")

    if not image:
        return json({"error": "Image file is required"}, status=400)

    calorie = await GetCalorieUseCase(request.app.ctx.calorie_repository).execute(
        meal, BytesIO(image.body)
    )

    return json(calorie.to_dict())
