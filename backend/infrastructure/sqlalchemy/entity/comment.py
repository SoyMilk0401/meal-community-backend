from dataclasses import dataclass

from backend.domain.entity.user import User


@dataclass
class Comment:
    id: int
    content: str
    """
    내용
    """
    author: User
    """
    작성자
    """
