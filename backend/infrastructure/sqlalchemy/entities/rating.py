from __future__ import annotations

from sqlalchemy import ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import Mapped, mapped_column

from backend.domain.entities.rating import Rating
from backend.infrastructure.sqlalchemy.base import Base

class RatingSchema(Base):
    __tablename__ = "rating"

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"))
    meal_id: Mapped[int] = mapped_column(ForeignKey("meal.id"))
    score: Mapped[int] = mapped_column()
    
    __table_args__ = (
        PrimaryKeyConstraint('meal_id', 'user_id'),
    )

    def to_entity(self) -> Rating:
        rating = Rating(
            user_id=self.user_id,
            meal_id=self.meal_id,
            score=self.score,
        )
        return rating