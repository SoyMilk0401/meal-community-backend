from abc import ABC, abstractmethod
from datetime import date

from backend.domain.entities.timetable import Timetable


class TimetableRepository(ABC):
    @abstractmethod
    async def get_by_code(
        self,
        school_name: str,
        edu_office_code: str,
        standard_school_code: str,
        date: date,
        grade: str,
        room: str,
    ) -> list[Timetable]:
        raise NotImplementedError

    @abstractmethod
    async def get_by_school_info_id(
        self,
        school_info_id: int,
        date: date,
        grade: int,
        room: int,
    ) -> list[Timetable]:
        raise NotImplementedError

    @abstractmethod
    async def create(
        self,
        school_info_id: int,
        timetable: Timetable,
    ) -> Timetable:
        raise NotImplementedError
