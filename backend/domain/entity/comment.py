from dataclasses import dataclass

from backend.domain.entity.user import User


@dataclass
class Comment:
    content: str
    """내용"""
    author: User
    """작성자"""
    created_at: str
    """생성일"""
