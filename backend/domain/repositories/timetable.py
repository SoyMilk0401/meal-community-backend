from abc import ABC, abstractmethod
from datetime import date

from backend.domain.entities.timetable import Timetable

class TimetableRepository(ABC):
    @abstractmethod
    async def get_by_code(
        school_name: str,
        edu_office_code: str,
        standard_school_code: str,
        date: date,
        grade: int,
        room: int
    ) -> list[Timetable]:
        raise NotImplementedError
    
    @abstractmethod
    async def create_by_code(self, timetable: Timetable) -> Timetable:
        raise NotImplementedError