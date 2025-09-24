from backend.application.exceptions import RatingNotFound
from backend.domain.entities.rating import Rating
from backend.domain.repositories.rating import RatingRepository


class GetRatingByMealIdUseCase:
    def __init__(self, raing_repository: RatingRepository):
        self.raing_repository = raing_repository
        
    async def execute(self, meal_id: int) -> list[Rating]:
        ratings = await self.raing_repository.get_by_meal_id(meal_id)
        if not ratings:
            raise RatingNotFound
        return ratings
    