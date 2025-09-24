from dataclasses import asdict, dataclass, field
from datetime import datetime
from backend.domain.entities.user import User
from backend.domain.utils import dict_factory

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

    def to_dict(self):
        return asdict(self, dict_factory=dict_factory)