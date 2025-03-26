from backend.application.exceptions import UserAlreadyExists, UserNotFound
from backend.domain.entities.user import User
from backend.domain.repository.user import UserRepository
from backend.application.use_cases.get.user import GetByEmailWithPasswordUserUseCase


class CreateUserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def execute(self, user: User):
        try:
            await GetByEmailWithPasswordUserUseCase(self.user_repository).execute(
                user.email, user.password
            )
        except UserNotFound:
            user = await self.user_repository.create(user)
            return user
        raise UserAlreadyExists
