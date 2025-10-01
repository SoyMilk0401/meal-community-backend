from backend.application.exceptions import RatingNotFound
from backend.domain.entities.rating import Rating
from backend.domain.repositories.rating import RatingRepository


class GetRatingByMealIdUseCase:
    def __init__(self, raing_repository: RatingRepository):
        self.raing_repository = raing_repository
        
    async def execute(self, meal_id: int) -> int:
        ratings = await self.raing_repository.get_by_meal_id(meal_id)
        
        if ratings:
            total_score = sum(rating.score for rating in ratings)
            average_score = total_score / len(ratings)
        else:
            average_score = 0
            raise RatingNotFound
        
        return round(average_score, 2)
    