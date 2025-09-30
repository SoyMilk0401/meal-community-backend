from backend.application.exceptions import AlreadyRated, UserNotFound
from backend.domain.entities.rating import Rating
from backend.domain.enum import CreateRaingStatus
from backend.domain.repositories.rating import RatingRepository


class CreateRatingUseCase:
    def __init__(self, raing_repository: RatingRepository):
        self.raing_repository = raing_repository
        
    async def execute(self, user_id: int, meal_id: int, rating: Rating) -> None:
        status = await self.raing_repository.create(
            user_id=user_id,
            meal_id=meal_id,
            rating=rating,
        )
        if status == CreateRaingStatus.AUTHOR_NOT_FOUND:
            raise UserNotFound
        if status == CreateRaingStatus.ALREADY_RATED:
            raise AlreadyRated