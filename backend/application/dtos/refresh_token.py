from dataclasses import dataclass


@dataclass
class GetRefreshTokenDTO:
    refresh_token: str
    user_id: int
