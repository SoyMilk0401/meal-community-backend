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
너는 전문 영양사야. 

[{food}] 대괄호 안에 담긴 메뉴는 식판에 담긴 예상 음식 목록이야.

너는 각 음식의 칼로리를 추정하고, 전체 칼로리 합계를 계산해야 해.

보통 음식은 식판에 담겨 나오고, 음식의 양을 최대한 고려서 칼로리를 추정해야 해.

다음의 경우는 total_calories를 0으로 설정하고 meals를 빈 배열로 만들어야 해:

1. 음식과 전혀 관련 없는 사진이거나, 음식이 전혀 보이지 않는 사진인 경우
2. 만약 주어진 메뉴와 사진 속 음식이 명확히 일치하지 않는 경우

그리고 meals 배열에는 각 음식의 이름과 추정 칼로리를 포함해야 해.
음식의 이름은 내가 제공한 메뉴 이름과 동일하게 유지해야 해.
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
