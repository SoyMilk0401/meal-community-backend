from backend.application.exceptions import UserNotFound
from backend.domain.entities.user import User
from backend.domain.repository.user import UserRepository


class GetByEmailWithPasswordUserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def execute(
        self,
        email: str,
        password: str,
    ) -> User:
        user = await self.user_repository.get_by_email_with_password(email, password)
        if not user:
            raise UserNotFound
        return user


class GetByIdUserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def execute(self, user_id: int) -> User:
        return await self.user_repository.get_by_id(user_id)
