from sanic import json
from sanic.blueprints import Blueprint
from sanic_ext import validate

from backend.application.dtos.meal import MealDTO
from backend.application.use_cases.get.meal import (
    GetDailyMealUseCase,
    GetWeeklyMealUseCase,
)
from backend.infrastructure.sanic import BackendRequest


meal = Blueprint("meal_endpoint", url_prefix="/meal")


@meal.post("/daily")
@validate(json=MealDTO, body_argument="meal_dto")
async def get_daily_meal(request: BackendRequest, meal_dto: MealDTO):
    results = await GetDailyMealUseCase(request.app.ctx.meal_repository).execute(
        meal_dto.edu_office_code,
        meal_dto.standard_school_code,
        meal_dto.date,
    )

    return json(
        {
            "results": [result.to_dict() for result in results],
        }
    )


@meal.post("/weekly")
@validate(json=MealDTO, body_argument="meal_dto")
async def get_weekly_meal(request: BackendRequest, meal_dto: MealDTO):
    results = await GetWeeklyMealUseCase(request.app.ctx.meal_repository).execute(
        meal_dto.edu_office_code,
        meal_dto.standard_school_code,
        meal_dto.date,
    )

    return json(
        {
            "results": [[meal.to_dict() for meal in meals] for meals in results],
        }
    )
