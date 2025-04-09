from dataclasses import asdict, dataclass
from datetime import datetime

from backend.domain.utils import dict_factory


@dataclass
class Meal:
    edu_office_code: str
    """시도교육청코드"""
    standard_school_code: str
    """표준학교코드"""
    school_name: str
    """학교명"""

    name: str
    """식사명"""
    dish_name: str
    """요리명"""
    calorie: str
    """칼로리"""

    date: datetime
    """급식일자"""

    def to_dict(self):
        return asdict(self, dict_factory=dict_factory)
