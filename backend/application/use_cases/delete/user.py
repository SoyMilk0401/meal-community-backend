from backend.infrastructure.sqlalchemy.repositories.user import (
    SQLAlchemyUserRepository,
)

class DeleteUserUseCase:
    def __init__(self, user_repository: SQLAlchemyUserRepository):
        self.user_repository = user_repository

    async def execute(self, user_id: int) -> None:
        return await self.user_repository.delete(user_id)