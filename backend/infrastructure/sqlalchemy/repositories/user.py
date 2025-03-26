from backend.domain.entities.user import User
from backend.infrastructure.sqlalchemy.entities.user import UserSchema
from backend.domain.repository.user import UserRepository
from backend.infrastructure.sqlalchemy import SQLAlchemy
from sqlalchemy import select
from sqlalchemy.orm import selectinload


class SQLAlchemyUserRepository(UserRepository):
    def __init__(self, sa: SQLAlchemy):
        self.sa = sa

    async def create(self, user: User) -> User:
        async with self.sa.session_maker() as session:
            async with session.begin():
                session.add(UserSchema.from_entity(user))
            await session.commit()
            return user

    async def get_by_email_with_password(
        self, email: str, password: str
    ) -> User | None:
        async with self.sa.session_maker() as session:
            async with session.begin():
                result = await session.execute(
                    select(UserSchema)
                    .where(UserSchema.email == email, UserSchema.password == password)
                    .options(selectinload(UserSchema.school_info))
                )

                user = result.scalars().first()

                if user:
                    return user.to_entity()

    async def get_by_id(self, user_id: int) -> User:
        async with self.sa.session_maker() as session:
            async with session.begin():
                result = await session.execute(
                    select(UserSchema).where(UserSchema.id == user_id)
                )

                user = result.scalar_one()
                return user.to_entity()
