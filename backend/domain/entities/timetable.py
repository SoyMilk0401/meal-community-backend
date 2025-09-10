from dataclasses import dataclass
from datetime import date


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