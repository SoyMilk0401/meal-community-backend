from dataclasses import asdict, dataclass
from datetime import date

from backend.domain.utils import dict_factory


@dataclass
class Timetable:
    date: date
    """시간표일자"""

    grade: int
    """학년"""
    room: int
    """반"""

    period: int
    """교시"""
    subject: str
    """과목명"""

    def to_dict(self):
        return asdict(self, dict_factory=dict_factory)
