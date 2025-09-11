from datetime import date

from neispy import Neispy
from neispy.error import DataNotFound

from backend.domain.entities.timetable import Timetable
from backend.domain.repositories.timetable import TimetableRepository
from backend.infrastructure.datetime import to_yyyymmdd
from backend.infrastructure.neispy.entities.timetable import NeispyTimetable


class NeispyTimetableRepository(TimetableRepository):
    def __init__(self, neispy: Neispy):
        self.neispy = neispy

    async def get_by_code(
        self,
        school_name: str,
        edu_office_code: str,
        standard_school_code: str,
        date: date,
        grade: str,
        room: str,
    ) -> list[Timetable]:

        try:
            if school_name.endswith("고등학교"):
                func = self.neispy.hisTimetable
            elif school_name.endswith("중학교"):
                func = self.neispy.misTimetable
            elif school_name.endswith("초등학교"):
                func = self.neispy.elsTimetable
            else:
                func = self.neispy.spsTimetable

            ay = date.year if date.month >= 3 else date.year - 1
            sem = 1 if 2 < date.month < 9 else 2

            timetables = await func(
                ATPT_OFCDC_SC_CODE=edu_office_code,
                SD_SCHUL_CODE=standard_school_code,
                ALL_TI_YMD=int(to_yyyymmdd(date)),
                GRADE=grade,
                CLASS_NM=room,
                AY=str(ay),
                SEM=str(sem),
            )

        except DataNotFound:
            return []

        response = next(iter(timetables.__dict__.values()))

        return [NeispyTimetable.from_neispy(timetable) for timetable in response[1].row]

    async def get_by_school_info_id(
        self,
        school_info_id: int,
        date: date,
        grade: int,
        room: int,
    ) -> list[Timetable]:
        raise NotImplementedError

    async def create(
        self,
        school_info_id: int,
        timetable: Timetable,
    ) -> Timetable:
        raise NotImplementedError
