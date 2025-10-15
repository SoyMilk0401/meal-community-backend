from backend.domain.repositories.rating import RatingRepository


class GetRatingByMealIdUseCase:
    def __init__(self, rating_repository: RatingRepository):
        self.rating_repository = rating_repository
        
    async def execute(self, meal_id: int) -> int:
        ratings = await self.rating_repository.get_by_meal_id(meal_id)
        
        if ratings:
            total_score = sum(rating.score for rating in ratings)
            average_score = total_score / len(ratings)
        else:
            average_score = 0
        
        return round(average_score, 2)
    