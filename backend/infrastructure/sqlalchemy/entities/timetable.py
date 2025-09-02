from __future__ import annotations

from datetime import date

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.domain.entities.timetable import Timetable
from backend.infrastructure.sqlalchemy.base import Base
from backend.infrastructure.sqlalchemy.mixin import Schema
from backend.infrastructure.sqlalchemy.entities.school_info import SchoolInfoSchema

class TimetableSchema(Base, Schema):
    __tablename__ = "timetable"

    school_info_id: Mapped[int] = mapped_column(
        ForeignKey("school_info.id"),
        nullable=False,
    )
    
    date: Mapped[date] = mapped_column()
    """시간표일자"""

    grade: Mapped[str] = mapped_column()
    """학년"""
    room: Mapped[str] = mapped_column()
    """학급명"""
    period: Mapped[str] = mapped_column()
    """교시"""
    subject: Mapped[str] = mapped_column()
    """과목명"""
    
    school_info: Mapped[SchoolInfoSchema] = relationship(
        back_populates="timetables"
    )
    
    def to_entity(self) -> Timetable:
        return Timetable(
            date=self.date,
            grade=self.grade,
            room=self.room,
            period=self.period,
            subject=self.subject,
        )