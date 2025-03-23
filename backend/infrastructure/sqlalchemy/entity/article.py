from dataclasses import dataclass

from backend.domain.entity.user import User


@dataclass
class Article:
    id: int
    title: str
    """
    제목
    """
    content: str
    """
    내용
    """
    author: User
    """
    작성자
    """
