from io import IOBase
from json import loads

import pydantic
from google.genai.client import AsyncClient

from backend.domain.entities.calorie import Calorie, Menu
from backend.domain.entities.meal import Meal
from backend.domain.repositories.calorie import CalorieRepository


class MenuResponse(pydantic.BaseModel):
    name: str
    calories: int | None


class CalorieResponse(pydantic.BaseModel):
    meals: list[MenuResponse]
    total_calories: int


PROMPT = """
너는 전문 영양사야. [{food}] 대괄호 안에 담긴 메뉴는 식판에 담긴 예상 음식 목록이야.

실제 사진에 담긴 식판을 보고, 음식의 종류와 양을 추론해서 상단의 JSON 형식으로 결과를 반환해줘.

최대한 칼로리와 음식의 종류를 정확하게 추론해줘.

만약 그럼에도 불구하고 음식의 종류나 칼로리를 정확하게 알 수 없고, 음식과 관련된 사진이 아니라면 null 또는 비어있는 응답을 반환해줘.
"""


class GeminiCalorieRepository(CalorieRepository):
    def __init__(self, client: AsyncClient) -> None:
        self.client = client

    async def get_calories(self, meal: Meal, image: IOBase) -> Calorie | None:
        menus = ", ".join(meal.dish_name.split("<br/>"))
        file = await self.client.files.upload(
            file=image,
            config={
                "mime_type": "image/jpeg",
            },
        )

        response = await self.client.models.generate_content(  # pyright: ignore[reportUnknownMemberType]
            model="gemini-2.5-flash",
            contents=[file, PROMPT.format(food=menus)],
            config={
                "response_mime_type": "application/json",
                "response_schema": CalorieResponse,
            },
        )

        if not response.text:
            return None

        data = loads(response.text)

        if not data["total_calories"]:
            return None

        meals = [
            Menu(name=menu["name"], calories=menu["calories"]) for menu in data["meals"]
        ]
        total_calories = data["total_calories"]

        return Calorie(meals=meals, total_calories=total_calories)
