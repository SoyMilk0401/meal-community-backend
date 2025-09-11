from dataclasses import dataclass

from neispy.domain.histimetable import HisTimeTableRow
from neispy.domain.mistimetable import MisTimeTableRow
from neispy.domain.elstimetable import ElsTimeTableRow
from neispy.domain.spstimetable import SpsTimeTableRow

from backend.domain.entities.timetable import Timetable
from backend.infrastructure.datetime import to_date


@dataclass
class NeispyTimetable(Timetable):
    @classmethod
    def from_neispy(
        cls,
        timetable: HisTimeTableRow | MisTimeTableRow | ElsTimeTableRow | SpsTimeTableRow,
    ) -> Timetable:
        return cls(
            date=to_date(timetable.ALL_TI_YMD),
            grade=timetable.GRADE,
            room=timetable.CLASS_NM,
            period=timetable.PERIO,
            subject=timetable.ITRT_CNTNT,
        )