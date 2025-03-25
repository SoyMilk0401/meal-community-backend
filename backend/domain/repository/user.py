from abc import ABC

from backend.domain.entity.user import User


class UserRepository(ABC):
    async def create(self, user: User) -> User:
        raise NotImplementedError

    async def get(self, email: str, password: str) -> User:
        raise NotImplementedError

    async def get_by_id(self, user_id: int) -> User:
        raise NotImplementedError

    async def delete(self, user: User) -> None:
        raise NotImplementedError
