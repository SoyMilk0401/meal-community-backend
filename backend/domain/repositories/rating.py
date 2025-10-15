from abc import ABC, abstractmethod

from backend.domain.entities.rating import Rating
from backend.domain.enum import CreateRatingStatus

class RatingRepository(ABC):
    @abstractmethod
    async def create(
        self,
        user_id: int,
        meal_id: int,
        rating: Rating,
    ) -> CreateRatingStatus:
        raise NotImplementedError
    
    @abstractmethod
    async def get_by_meal_id(
        self, meal_id: int
    ) -> list[Rating]:
        raise NotImplementedError
