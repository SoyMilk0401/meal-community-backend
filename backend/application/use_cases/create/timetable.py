from backend.domain.entities.timetable import Timetable
from backend.domain.repositories.timetable import TimetableRepository


class CreateTimetableUseCase:
    def __init__(self, timetable_repository: TimetableRepository):
        self.timetable_repository = timetable_repository

    async def execute(
        self,
        school_info_id: int,
        timetable: Timetable,
    ) -> int:
        result = await self.timetable_repository.create(
            school_info_id=school_info_id,
            timetable=timetable,
        )

        return result
