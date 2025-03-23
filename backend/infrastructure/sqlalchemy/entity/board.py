from dataclasses import dataclass

from backend.domain.entity.article import Article


@dataclass
class Board:
    id: int
    title: str
    """
    제목
    """
    content: Article
    """
    내용
    """
