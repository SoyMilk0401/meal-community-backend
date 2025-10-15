from dataclasses import asdict, dataclass

from backend.domain.utils import dict_factory


@dataclass
class CreateRatingDTO:
    meal_id: int
    """급식 ID"""
    score: int
    """평점"""
    
    def to_dict(self):
        return asdict(self, dict_factory=dict_factory)