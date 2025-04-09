from sanic import json
from sanic.blueprints import Blueprint
from sanic_ext import validate

from backend.application.dtos.meal import WeeklyMealDTO
from backend.application.use_cases.get.meal import GetWeeklyMealUseCase
from backend.infrastructure.sanic import BackendRequest


meal = Blueprint("meal_endpoint", url_prefix="/meal")


@meal.get("/weekly")
@validate(json=WeeklyMealDTO, body_argument="weekly_meal_dto")
async def get_weekly_meal(request: BackendRequest, weekly_meal_dto: WeeklyMealDTO):
    """
    Get weekly meal for a given school and date.
    """
    results = await GetWeeklyMealUseCase(request.app.ctx.meal_repository).execute(
        weekly_meal_dto.edu_office_code,
        weekly_meal_dto.standard_school_code,
        weekly_meal_dto.date,
    )

    return json(
        {
            "results": [result.to_dict() for result in results],
        }
    )
