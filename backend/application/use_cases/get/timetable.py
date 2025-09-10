from datetime import timedelta
from backend.application.exceptions import TimetableNotFound
from backend.domain.entities.timetable import Timetable
from backend.domain.repositories.timetable import TimetableRepository 
from backend.infrastructure.datetime import to_date


class GetWeeklyTimetableUseCase:
    def __init__(self, timetable_repository: TimetableRepository):
        self.timetable_repository = timetable_repository

    async def execute(
        self, 
        school_info_id: int,
        current_date: str,
        grade: int,
        room: int
    ) -> list[list[Timetable]]:
        
        current_datetime = to_date(current_date)
        dates = [
            current_datetime.date + timedelta(days=i)
            for i in range(-current_datetime.date.weekday(), 5 - current_datetime.date.weekday())
        ]
        
        timetables = []
        for date in dates:
            daily_timetables = await self.timetable_repository.get_by_code(
                school_info_id=school_info_id,
                date=date,
                grade=grade,
                room=room,
            )
            if not daily_timetables:
                raise TimetableNotFound
            timetables.append(daily_timetables)
        
        return timetables


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