from datetime import date
from typing import Literal

from neispy import Neispy
from neispy.error import DataNotFound

from backend.domain.entities.timetable import Timetable
from backend.domain.entities.school_info import SchoolInfo
from backend.domain.repositories.timetable import TimetableRepository


class NeispyTimetableRepository(TimetableRepository):
    def __init__(self, neispy: Neispy):
        self.neispy = neispy
        
    async def get_by_code(
        self,
        school_info: SchoolInfo,
        date: date,
        grade: str,
        room: str
    ) -> list[Timetable]:
        
        