from sqlalchemy import select

from backend.domain.entities.rating import Rating
from backend.domain.enum import CreateRatingStatus
from backend.domain.repositories.rating import RatingRepository
from backend.infrastructure.sqlalchemy import SQLAlchemy
from backend.infrastructure.sqlalchemy.entities.meal import MealSchema
from backend.infrastructure.sqlalchemy.entities.rating import RatingSchema


class SQLAlchemyRatingRepository(RatingRepository):
    def __init__(self, sa: SQLAlchemy):
        self.sa = sa

    async def create(
        self,
        user_id: int,
        meal_id: int,
        rating: Rating,
    ) -> CreateRatingStatus:
        async with self.sa.session_maker() as session:
            async with session.begin():
                meal = await session.execute(
                    select(MealSchema).where(MealSchema.id == meal_id)
                )
                if not meal.scalar_one_or_none():
                    return CreateRatingStatus.MEAL_INFO_NOT_FOUND
                
                existing_rating = await session.execute(
                    select(RatingSchema).where(
                        RatingSchema.meal_id == meal_id,
                        RatingSchema.user_id == user_id
                    )
                )
                if existing_rating.scalar_one_or_none():
                    return CreateRatingStatus.ALREADY_RATED
                    
                rating_schema = RatingSchema(
                    meal_id=meal_id,
                    user_id=user_id,
                    score=rating.score,
                )
                session.add(rating_schema)
                
                await session.commit()
                return CreateRatingStatus.SUCCESS

    async def get_by_meal_id(self, meal_id: int) -> list[Rating]:
        async with self.sa.session_maker() as session:
            async with session.begin():
                result = await session.execute(
                    select(RatingSchema)
                    .where(RatingSchema.meal_id == meal_id)
                )
                ratings = result.scalars().all()

                return [rating.to_entity() for rating in ratings]