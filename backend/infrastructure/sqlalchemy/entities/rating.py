from __future__ import annotations
from datetime import datetime
from sqlalchemy import ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from backend.domain.entities.rating import Rating
from backend.infrastructure.sqlalchemy.base import Base
from backend.infrastructure.sqlalchemy.entities.user import UserSchema

class RatingSchema(Base):
    __tablename__ = "rating"

    meal_id: Mapped[int] = mapped_column(ForeignKey("meal.id"), primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), primary_key=True)
    score: Mapped[int] = mapped_column()

    author: Mapped[UserSchema] = relationship(
        "UserSchema", uselist=False, lazy="selectin"
    )

    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())

    def to_entity(self) -> Rating:
        rating = Rating(
            meal_id=self.meal_id,
            score=self.score,
            author=self.author.to_entity(),
        )
        rating.created_at = self.created_at
        return rating