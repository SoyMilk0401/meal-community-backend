from backend.domain.entities.user import User
from backend.domain.repositories.user import UserRepository


class UpdateUserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def execute(self, user: User) -> User:
        return await self.user_repository.update(user)