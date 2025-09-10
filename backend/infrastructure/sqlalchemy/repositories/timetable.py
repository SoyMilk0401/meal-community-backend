from datetime import date

from sqlalchemy import select

from backend.domain.entities.school_info import SchoolInfo
from backend.domain.entities.timetable import Timetable
from backend.domain.repositories.timetable import TimetableRepository
from backend.infrastructure.sqlalchemy import SQLAlchemy
from backend.infrastructure.sqlalchemy.entities.school_info import SchoolInfoSchema
from backend.infrastructure.sqlalchemy.entities.timetable import TimetableSchema


class SQLAlchemyTimetableRepository(TimetableRepository):
    def __init__(self, sa: SQLAlchemy):
        self.sa = sa
    
    async def get_by_code(
        self,
        school_name: str,
        edu_office_code: str,
        standard_school_code: str,
        date: date,
        grade: int,
        room: int,
    ) -> list[Timetable]:
        async with self.sa.session_maker() as session:
            async with session.begin():
                result = await session.execute(
                    select(TimetableSchema).where(
                        TimetableSchema.school_info.has(
                            SchoolInfo.name == school_name,
                            SchoolInfo.edu_office_code == edu_office_code,
                            SchoolInfo.standard_school_code == standard_school_code,
                        ),
                        TimetableSchema.date == date,
                        TimetableSchema.grade == grade,
                        TimetableSchema.room == room,
                    )
                )
                return [schema.to_entity() for schema in result.scalars().all()]

    async def create(
        self,
        school_info_id: int,
        timetable: Timetable,
    ) -> Timetable:
        async with self.sa.session_maker() as session:
            async with session.begin():
                timetable_schema = TimetableSchema(
                    school_info_id=school_info_id,
                    date=timetable.date,
                    grade=timetable.grade,
                    room=timetable.room,
                    data=timetable.data,
                )
                session.add(timetable_schema)
                await session.commit()
                return timetable_schema.id