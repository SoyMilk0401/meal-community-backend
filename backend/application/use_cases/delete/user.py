from backend.domain.repositories.user import UserRepository


class DeleteUserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def execute(self, user_id: int) -> None:
        await self.user_repository.delete(user_id)