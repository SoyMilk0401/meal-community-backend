from datetime import datetime
from neispy import Neispy

from backend.domain.entities.meal import Meal
from backend.domain.repositories.meal import MealRepository
from backend.infrastructure.neispy.entities.meal import NeispyMeal
from backend.infrastructure.datetime import to_yyyymmdd


class NeispyMealRepository(MealRepository):
    def __init__(self, neispy: Neispy):
        self.neispy = neispy

    async def get_meal_by_code(
        self, edu_office_code: str, standard_school_code: str, date: datetime
    ) -> Meal:

        info = await self.neispy.mealServiceDietInfo(
            ATPT_OFCDC_SC_CODE=edu_office_code,
            SD_SCHUL_CODE=standard_school_code,
            MLSV_YMD=to_yyyymmdd(date),
        )

        return NeispyMeal.from_neispy(
            info.mealServiceDietInfo[1].row[0], edu_office_code, standard_school_code
        )
