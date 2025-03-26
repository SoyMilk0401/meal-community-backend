from abc import ABC
from typing import Optional

from backend.domain.entities.user import User


class UserRepository(ABC):
    async def create(self, user: User) -> User:
        raise NotImplementedError

    async def get_by_email_with_password(
        self, email: str, password: str
    ) -> Optional[User]:
        raise NotImplementedError

    async def get_by_id(self, user_id: int) -> User:
        raise NotImplementedError

    async def delete(self, user: User) -> None:
        raise NotImplementedError
