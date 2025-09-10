from datetime import timedelta
from sanic import json
from sanic.blueprints import Blueprint
from sanic_ext import validate
from backend.infrastructure.datetime import to_date

from backend.application.dtos.timetable import TimetableDTO
from backend.application.exceptions import TimetableNotFound
from backend.application.use_cases.create.timetable import CreateTimetableUseCase
from backend.application.use_cases.get.timetable import (
    GetDailyTimetableUseCase,
    GetWeeklyTimetableUseCase,
)
from backend.application.use_cases.get.user import GetUserByIDUseCase
from backend.application.use_cases.get.school_info import GetSchoolInfoUseCase
from backend.infrastructure.jwt import require_auth
from backend.infrastructure.sanic import BackendRequest

timetable = Blueprint('timetable_endpoint', url_prefix='/timetable')


@timetable.post("/weekly")
@validate(json=TimetableDTO, body_argument="timetable_dto")
@require_auth
async def get_weekly_timetable(request: BackendRequest, user_id: str, timetable_dto: TimetableDTO):
    user = await GetUserByIDUseCase(request.app.ctx.user_repository).execute(
        int(user_id)
    )
    
    school_info_id = await GetSchoolInfoUseCase(request.app.ctx.school_info_repository).execute(
        user.school_info.edu_office_code,
        user.school_info.standard_school_code,
    )
    
    current_datetime = to_date(timetable_dto)
    dates = [
        current_datetime + timedelta(days=i)
        for i in range(-current_datetime.weekday(), 5 - current_datetime.weekday())
    ]
    
    async with request.app.ctx.lock:
        results = []
        for date in dates:
            try:
                daily = await GetDailyTimetableUseCase(
                    request.app.ctx.timetable_repository
                ).execute(
                    school_info_id=school_info_id,
                    grade=user.grade,
                    room=user.room,
                    current_date=date,
                )
                results.append(daily)
                continue
            except TimetableNotFound:
                daily = await GetDailyTimetableUseCase(
                    request.app.ctx.neispy_timetable_repository
                ).execute(
                    school_info_id=school_info_id,
                    grade=user.grade,
                    room=user.room,
                    current_date=date,
                )
                
                await CreateTimetableUseCase(request.app.ctx.timetable_repository).execute(
                    school_info_id=school_info_id,
                    timetable=daily,
                )
                results.append(daily)
        
        return json(
            {
                "results": [[item.to_dict() for item in daily] for daily in results],
            }
        )
                    