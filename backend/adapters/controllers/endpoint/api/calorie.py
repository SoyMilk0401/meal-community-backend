from io import BytesIO

from sanic import json
from sanic.blueprints import Blueprint
from sanic_ext import openapi

from backend.application.use_cases.get.calorie import GetCalorieUseCase
from backend.application.use_cases.get.meal import GetDailyMealByIDUseCase
from backend.infrastructure.jwt import require_auth
from backend.infrastructure.sanic import BackendRequest

calorie = Blueprint("calorie_endpoint", url_prefix="/calorie")


@openapi.body(
    {
        "type": "object",
        "properties": {
            "meal_id": {
                "type": "integer",
                "description": "ID of the meal to analyze",
            },
            "image": {
                "type": "string",
                "format": "binary",
                "description": "Image of the meal for calorie estimation",
            },
        },
        "required": ["meal_id", "image"],
    }
)
@calorie.post("/inference")
@require_auth
async def get_calories_by_meal_image(
    request: BackendRequest,
    _,
):
    meal = await GetDailyMealByIDUseCase(request.app.ctx.sa_meal_repository).execute(
        request.form.get("meal_id")
    )

    image = request.files.get("image")

    calorie = await GetCalorieUseCase(request.app.ctx.calorie_repository).execute(
        meal, BytesIO(image.body)
    )

    return json(calorie.to_dict())
