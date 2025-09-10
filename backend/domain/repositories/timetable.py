from abc import ABC, abstractmethod
from datetime import date

from backend.domain.entities.timetable import Timetable

class TimetableRepository(ABC):
    @abstractmethod
    async def get_by_code(
        school_info_id:int,
        date: date,
        grade: int,
        room: int
    ) -> list[Timetable]:
        raise NotImplementedError
    
    @abstractmethod
    async def create(self, timetable: Timetable) -> Timetable:
        raise NotImplementedError