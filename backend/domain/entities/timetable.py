from dataclasses import dataclass
from datetime import date

from backend.domain.entities.school_info import SchoolInfo

@dataclass
class Timetable:
    school_info: SchoolInfo
    """학교 정보"""
    date: date
    """시간표일자"""
    
    grade: str
    """학년"""
    room: str
    """반"""
    
    period: str
    """교시"""
    subject_name: str
    """과목명"""