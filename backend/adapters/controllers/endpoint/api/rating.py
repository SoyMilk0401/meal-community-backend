from sanic import json
from sanic.blueprints import Blueprint
from sanic_ext import validate

from backend.application.dtos.rating import CreateRatingDTO
from backend.application.exceptions import RatingNotFound
from backend.application.use_cases.create.rating import CreateRatingUseCase
from backend.application.use_cases.get.rating import GetRaingByMealTdUseCase
from backend.application.use_cases.get.user import GetUserByIDUseCase
from backend.domain.entities.rating import Rating
from backend.infrastructure.jwt import require_auth
from backend.infrastructure.sanic import BackendRequest


rating = Blueprint("rating", url_prefix="/rating")


@rating.post("/write")
@validate(json=CreateRatingDTO, body_argument="create_rating_dto")
@require_auth
async def write_rating(
    request: BackendRequest,
    user_id: int,
    create_rating_dto: CreateRatingDTO,
):
    user = await GetUserByIDUseCase(request.app.ctx.user_repository).execute(user_id)

    rating_entity = Rating(
        meal_id=create_rating_dto.meal_id,
        author=user,
        score=create_rating_dto.score
    )
    
    await CreateRatingUseCase(request.app.ctx.rating_repository).execute(
        user_id=user_id,
        meal_id=create_rating_dto.meal_id,
        rating=rating_entity,
    )
    
    return json({"message": "Rating created successfully"})


@rating.get("/<meal_id:int>")
@require_auth
async def get_ratings_by_meal_id(
    request: BackendRequest,
    _,
    meal_id: int,
):
    try:
        ratings = await GetRaingByMealTdUseCase(
            request.app.ctx.rating_repository
        ).excute(meal_id)
    except RatingNotFound:
        return json({"results": []})
    
    result = [rating for rating in ratings]
    
    return json({"results": [rating.to_dict() for rating in result]})