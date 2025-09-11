from datetime import date, timedelta
from backend.application.exceptions import TimetableNotFound
from backend.application.use_cases.create.timetable import CreateTimetableUseCase
from backend.application.use_cases.get.school_info import GetSchoolInfoUseCase
from backend.domain.entities.timetable import Timetable
from backend.domain.entities.user import User
from backend.domain.repositories.timetable import TimetableRepository


class GetDailyTimetableUseCase:
    def __init__(self, sa_timetable_repository: TimetableRepository, remote_timetable_repository: TimetableRepository):
        self.sa_timetable_repository = sa_timetable_repository
        self.remote_timetable_repository = remote_timetable_repository

    async def execute(
        self, 
        user: User,
        school_info_id: int,
        date: date
    ) -> list[Timetable]:
        
        timetables = await self.sa_timetable_repository.get_by_code(
            school_info_id=school_info_id,
            date=date,
            grade=user.grade,
            room=user.room,
        )
        
        if not timetables:
            timetables = await self.remote_timetable_repository.get_by_code(
                school_name=user.school_info.name,
                edu_office_code=user.school_info.edu_office_code,
                standard_school_code=user.school_info.standard_school_code,
                date=date,
                grade=str(user.grade),
                room=str(user.room),
            )
            
            if timetables:
                create_use_case = CreateTimetableUseCase(self.sa_timetable_repository)
                for timetable in timetables:
                    await create_use_case.execute(school_info_id, timetable)

        if not timetables:
            raise TimetableNotFound
        
        return timetables