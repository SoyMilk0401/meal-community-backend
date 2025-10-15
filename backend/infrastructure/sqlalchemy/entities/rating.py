from __future__ import annotations
from datetime import datetime
from sqlalchemy import ForeignKey, DateTime, PrimaryKeyConstraint, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from backend.domain.entities.rating import Rating
from backend.infrastructure.sqlalchemy.base import Base
from backend.infrastructure.sqlalchemy.entities.user import UserSchema

class RatingSchema(Base):
    __tablename__ = "rating"

    meal_id: Mapped[int] = mapped_column(ForeignKey("meal.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    score: Mapped[int] = mapped_column()
    
    __table_args__ = (
        PrimaryKeyConstraint('meal_id', 'user_id'),
    )

    def to_entity(self) -> Rating:
        rating = Rating(
            meal_id=self.meal_id,
            score=self.score,
        )
        return rating