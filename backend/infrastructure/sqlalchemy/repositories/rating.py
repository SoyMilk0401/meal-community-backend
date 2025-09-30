from sqlalchemy import select
from sqlalchemy.orm import selectinload

from backend.domain.entities.rating import Rating
from backend.domain.enum import CreateRaingStatus
from backend.domain.repositories.rating import RatingRepository
from backend.infrastructure.sqlalchemy import SQLAlchemy
from backend.infrastructure.sqlalchemy.entities.rating import RatingSchema
from backend.infrastructure.sqlalchemy.entities.user import UserSchema


class SQLAlchemyRatingRepository(RatingRepository):
    def __init__(self, sa: SQLAlchemy):
        self.sa = sa

    async def create(
        self,
        user_id: int,
        meal_id: int,
        rating: Rating,
    ) -> CreateRaingStatus:
        async with self.sa.session_maker() as session:
            async with session.begin():
                existing_rating = await session.execute(
                    select(RatingSchema).where(
                        RatingSchema.meal_id == meal_id,
                        RatingSchema.user_id == user_id
                    )
                )
                if existing_rating.scalar_one_or_none():
                    return CreateRaingStatus.ALREADY_RATED

                author = await session.get(UserSchema, user_id)

                if not author:
                        return CreateRaingStatus.AUTHOR_NOT_FOUND
                    
                rating_schema = RatingSchema(
                    score=rating.score,
                    user_id=user_id,
                    meal_id=meal_id,
                    author=author
                )
                session.add(rating_schema)
                
                await session.commit()
                return CreateRaingStatus.SUCCESS

    async def get_by_meal_id(self, meal_id: int) -> list[Rating]:
        async with self.sa.session_maker() as session:
            async with session.begin():
                result = await session.execute(
                    select(RatingSchema)
                    .where(RatingSchema.meal_id == meal_id)
                    .options(selectinload(RatingSchema.author))
                )
                ratings = result.scalars().all()

                return [rating.to_entity() for rating in ratings]