from dataclasses import dataclass


@dataclass
class RefreshToken:
    user_id: int
    value: str
