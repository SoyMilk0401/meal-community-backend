from dataclasses import dataclass
from backend.application.dtos.school import InfoSchoolDTO


@dataclass
class MealDTO(InfoSchoolDTO):
    date: str
