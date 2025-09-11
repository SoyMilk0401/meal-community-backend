from dataclasses import asdict, dataclass, field
from datetime import date

from backend.domain.utils import dict_factory

@dataclass
class Timetable:
    date: date
    """시간표일자"""
    
    grade: str
    """학년"""
    room: str
    """반"""
    
    period: str
    """교시"""
    subject: str
    """과목명"""
    
    def to_dict(self):
        return asdict(self, dict_factory=dict_factory)