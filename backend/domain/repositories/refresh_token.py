from abc import ABC, abstractmethod

from backend.domain.entities.refresh_token import RefreshToken


class RefreshTokenRepository(ABC):
    @abstractmethod
    def __init__(self, expires_in: int):
        self.expires_in = expires_in

    @abstractmethod
    async def create_refresh_token(self, refresh_token: RefreshToken) -> RefreshToken:
        raise NotImplementedError

    @abstractmethod
    async def get_refresh_token(self, refresh_token_value: str) -> RefreshToken | None:
        raise NotImplementedError

    @abstractmethod
    async def delete_refresh_token(self, refresh_token_value: str) -> None:
        raise NotImplementedError

    @abstractmethod
    async def update_refresh_token_ttl(self, refresh_token_value: str) -> None:
        raise NotImplementedError
