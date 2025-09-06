from backend.application.exceptions import SchoolNotFound
from backend.domain.entities.timetable import Timetable
from backend.domain.enum import CreateTimetableStatus
from backend.domain.repositories.timetable import TimetableRepository


class CreateTimetableUseCase:
    def __init__(self, timetable_repository: TimetableRepository):
        self.timetable_repository = timetable_repository

    async def execute(
        self,
        school_name: str,
        edu_office_code: str,
        standard_school_code: str,
        timetable: Timetable,
    ) -> int:
        result = await self.timetable_repository.create_by_code(
            school_name=school_name,
            edu_office_code=edu_office_code,
            standard_school_code=standard_school_code,
            timetable=timetable,
        )

        if result == CreateTimetableStatus.SCHOOL_INFO_NOT_FOUND:
            raise SchoolNotFound

        return result