from backend.application.exceptions import IncorrectEmailOrPassword, UserNotFound
from backend.domain.entities.user import User
from backend.domain.repositories.user import UserRepository


class GetUserIDByEmail:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def execute(self, email: str) -> int:
        user_id = await self.user_repository.get_id_by_email(email)
        if not user_id:
            raise UserNotFound
        return user_id


class GetUserIDByEmailWithPassword:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def execute(
        self,
        email: str,
        password: str,
    ) -> int:
        user = await self.user_repository.get_id_by_email_with_password(email, password)
        if not user:
            raise IncorrectEmailOrPassword
        return user


class GetUserByIDUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def execute(self, user_id: int) -> User:
        return await self.user_repository.get_by_id(user_id)
