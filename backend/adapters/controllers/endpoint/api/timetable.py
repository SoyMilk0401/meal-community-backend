from datetime import timedelta
from sanic import json
from sanic.blueprints import Blueprint
from sanic_ext import validate

from backend.application.dtos.timetable import TimetableDTO
from backend.application.exceptions import TimetableNotFound
from backend.application.use_cases.create.timetable import CreateTimetableUseCase
from backend.application.use_cases.get.timetable import (
    GetDailyTimetableUseCase,
)
from backend.application.use_cases.get.user import GetUserByIDUseCase
from backend.application.use_cases.get.school_info import GetSchoolInfoUseCase
from backend.infrastructure.jwt import require_auth
from backend.infrastructure.sanic import BackendRequest

timetable = Blueprint('timetable_endpoint', url_prefix='/timetable')

# @timetable.post("/daily")
# @validate(json=TimetableDTO, body_argument="timetable_dto")
# @require_auth
# async def get_daily_timetable(request: BackendRequest, user_id: str, timetable_dto: TimetableDTO):
#     user = await GetUserByIDUseCase(request.app.ctx.user_repository).execute(
#         int(user_id)
#     )
    
#     user_info = {
#         "school_name": user.school_info.name,
#         "edu_office_code": user.school_info.edu_office_code,
#         "standard_school_code": user.school_info.standard_school_code,
#         "grade": user.grade,
#         "room": user.room,
#     }
    
    
#     async with request.app.ctx.lock:
#         try:
#             results = await GetWeeklyTimetableUseCase(
#                 request.app.ctx.timmetable_repository
#             ).execute(
#                 current_date=timetable_dto.date,
#                 **user_info
#             )
#         except TimetableNotFound:
#             remote_results = await GetWeeklyTimetableWithIDUseCase(
#                 request.app.ctx.neispy_timetable_repository
#             ).execute(
#                 current_date=timetable_dto.date,
#                 **user_info
#             )

#             results = [
#                 (
#                     await CreateTimetableUseCase(request.app.ctx.timmetable_repository).execute(
#                         **user_info,
#                         result=result,
#                     ),
#                     result,
#                 )
#                 for result in remote_results
#             ]

#     return json(
#         {
#             "results": [{"timetable_id": id, **result.to_dict()} for id, result in results],
#         }
#     )



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
    
    async with request.app.ctx.lock:
        dates = [
            timetable_dto.date + timedelta(days=i)
            for i in range(-timetable_dto.date.weekday(), 5 - timetable_dto.date.weekday())
        ]
        
        results = [
            await GetDailyTimetableUseCase(request.app.ctx.timmetable_repository).execute(
                school_info_id=school_info_id,
                grade=user.grade,
                room=user.room,
                current_date=date,
            )
            for date in dates
        ]
        
        for result in results:
            if not result:
                result = await GetDailyTimetableUseCase(
                    request.app.ctx.neispy_timetable_repository
                ).execute(
                    school_info_id=school_info_id,
                    grade=user.grade,
                    room=user.room,
                    current_date=timetable_dto.date,
                )
                
                await CreateTimetableUseCase(request.app.ctx.timmetable_repository).execute(
                    school_info_id=school_info_id,
                    timetable=result,
                )
                
        return json(
            {
                "results": [[item.to_dict() for item in daily] for daily in results],
            }
        )
                    