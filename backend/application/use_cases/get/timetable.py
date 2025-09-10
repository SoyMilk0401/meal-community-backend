from backend.application.exceptions import TimetableNotFound
from backend.domain.entities.timetable import Timetable
from backend.domain.repositories.timetable import TimetableRepository 
from backend.infrastructure.datetime import to_date


class GetDailyTimetableUseCase:
    def __init__(self, timetable_repository: TimetableRepository):
        self.timetable_repository = timetable_repository

    async def execute(
        self, 
        school_info_id: int,
        current_date: str,
        grade: int,
        room: int
    ) -> list[Timetable]:
        
        current_datetime = to_date(current_date)
        
        timetables = await self.timetable_repository.get_by_code(
            school_info_id=school_info_id,
            date=current_datetime,
            grade=grade,
            room=room,
        )
        
        if not timetables:
            raise TimetableNotFound
        
        return timetables