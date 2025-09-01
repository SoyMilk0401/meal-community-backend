from dataclasses import dataclass

from neispy.domain.histimetable import HisTimeTableRow
from neispy.domain.mistimetable import MisTimeTableRow
from neispy.domain.elstimetable import ElsTimeTableRow

from backend.domain.entities.timetable import Timetable
from backend.domain.entities.school_info import SchoolInfo
from backend.infrastructure.datetime import to_date


@dataclass
class NeispyTimetable(Timetable):
    @classmethod
    def from_neispy(
        cls,
        school_info: SchoolInfo,
        timetable: HisTimeTableRow | MisTimeTableRow | ElsTimeTableRow,
    ) -> Timetable:
        return cls(
            school_info=school_info,
            date=to_date(timetable.ALL_TI_YMD),
            grade=timetable.GRADE,
            room=timetable.CLASS_NM,
            period=timetable.PERIO,
            subject_name=timetable.ITRT_CNTNT,
        )