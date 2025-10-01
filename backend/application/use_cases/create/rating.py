from backend.application.exceptions import AlreadyRated, MealNotFound
from backend.domain.entities.rating import Rating
from backend.domain.enum import CreateRatingStatus
from backend.domain.repositories.rating import RatingRepository


class CreateRatingUseCase:
    def __init__(self, raing_repository: RatingRepository):
        self.raing_repository = raing_repository
        
    async def execute(self, meal_id: int, user_id: int, rating: Rating) -> None:
        status = await self.raing_repository.create(
            meal_id=meal_id,
            user_id=user_id,
            rating=rating,
        )
        if status == CreateRatingStatus.ALREADY_RATED:
            raise AlreadyRated
        if status == CreateRatingStatus.MEAL_INFO_NOT_FOUND:
            raise MealNotFound