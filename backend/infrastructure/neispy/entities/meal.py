from dataclasses import dataclass

from neispy.domain.mealservicedietinfo import MealServiceDietInfoRow

from backend.domain.entities.meal import Meal
from backend.infrastructure.datetime import to_datetime


@dataclass
class NeispyMeal(Meal):
    @classmethod
    def from_neispy(
        cls,
        meal: MealServiceDietInfoRow,
        edu_office_code: str,
        standard_school_code: str,
    ) -> Meal:
        return cls(
            edu_office_code=edu_office_code,
            standard_school_code=standard_school_code,
            name=meal.MMEAL_SC_NM,
            dish_name=meal.DDISH_NM,
            school_name=meal.SCHUL_NM,
            calorie=meal.CAL_INFO,
            date=to_datetime(meal.MLSV_FROM_YMD),
        )
