import asyncio
from datetime import timedelta

from backend.application.exceptions import TimetableNotFound
from backend.domain.entities.timetable import Timetable
from backend.domain.repositories.timetable import TimetableRepository 
from backend.infrastructure.datetime import to_date


class GetDailyTimetableUseCase:
    def __init__(self, timetable_repository: TimetableRepository):
        self.timetable_repository = timetable_repository

    async def execute(
        self, 
        school_name: str,
        edu_office_code: str,
        standard_school_code: str,
        current_date: str,
        grade: int,
        room: int
    ) -> list[Timetable]:
        
        current_datetime = to_date(current_date)
        
        timetables = await self.timetable_repository.get_by_code(
            school_name=school_name,
            edu_office_code=edu_office_code,
            standard_school_code=standard_school_code,
            date=current_datetime,
            grade=grade,
            room=room,
        )
        
        if not timetables:
            raise TimetableNotFound
        
        return timetables

class GetWeeklyTimetableUseCase:
    def __init__(self, timetable_repository: TimetableRepository):
        self.timetable_repository = timetable_repository
        
    async def execute(
        self, 
        school_name: str,
        edu_office_code: str,
        standard_school_code: str,
        current_date: str,
        grade: int,
        room: int
    ) -> list[Timetable]:
        
        current_datetime = to_date(current_date)
        dates = [
            current_datetime + timedelta(days=i)
            for i in range(-current_datetime.weekday(), 5 - current_datetime.weekday())
        ]
        
        timetables = await asyncio.gather(
            *[
                self.timetable_repository.get_by_code(
                    school_name=school_name,
                    edu_office_code=edu_office_code,
                    standard_school_code=standard_school_code,
                    date=date,
                    grade=grade,
                    room=room,
                )
                for date in dates
            ]
        )
        
        if not any(timetable for timetable in timetables):
            raise TimetableNotFound
        
        return timetables