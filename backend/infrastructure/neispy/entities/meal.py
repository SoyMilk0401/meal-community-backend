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
    ) -> Meal:
        return cls(
            name=meal.MMEAL_SC_NM,
            dish_name=meal.DDISH_NM,
            calorie=meal.CAL_INFO,
            date=to_datetime(meal.MLSV_FROM_YMD),
        )
