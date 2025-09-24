from dataclasses import dataclass, field
from datetime import datetime
from backend.domain.entities.user import User

@dataclass
class Rating:
    meal_id: int
    """급식 ID"""
    author: User
    """작성자"""
    score: int
    """평점"""
    created_at: datetime = field(init=False)
    """생성일"""