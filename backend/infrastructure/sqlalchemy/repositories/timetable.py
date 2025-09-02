from datetime import date

from backend.domain.entities.timetable import Timetable
from backend.domain.repositories.timetable import TimetableRepository
from backend.infrastructure.sqlalchemy import SQLAlchemy
from backend.infrastructure.sqlalchemy.entities.timetable import TimetableSchema


class SQLAlchemyTimetableRepository:
    def __init__(self, sa: SQLAlchemy):
        self.sa = sa
        
    async def create(
        self,
        
    )
        
    async def get_by_code(
        self, edu_office_code: str, standard_school_code: str, date: date
    ) -> list[Timetable]:
        ...