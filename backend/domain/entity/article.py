from dataclasses import dataclass

from backend.domain.entity.user import User
from backend.domain.entity.comment import Comment


@dataclass
class Article:
    title: str
    """제목"""
    content: str
    """내용"""
    author: User
    """작성자"""
    comments: list[Comment]
    """댓글"""
    created_at: str
    """생성일"""
