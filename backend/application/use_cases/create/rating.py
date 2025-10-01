from backend.application.exceptions import AlreadyRated, InvalidRatingRange, MealNotFound
from backend.domain.entities.rating import Rating
from backend.domain.enum import CreateRatingStatus
from backend.domain.repositories.rating import RatingRepository


class CreateRatingUseCase:
    def __init__(self, rating_repository: RatingRepository):
        self.rating_repository = rating_repository
        
    async def execute(self, meal_id: int, user_id: int, rating: Rating) -> None:
        if rating.score < 0 or rating.score > 5:
            raise InvalidRatingRange
        
        status = await self.rating_repository.create(
            meal_id=meal_id,
            user_id=user_id,
            rating=rating,
        )
        if status == CreateRatingStatus.ALREADY_RATED:
            raise AlreadyRated
        if status == CreateRatingStatus.MEAL_INFO_NOT_FOUND:
            raise MealNotFound