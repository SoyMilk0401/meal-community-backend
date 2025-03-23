from dataclasses import dataclass

from backend.domain.entity.article import Article


@dataclass
class Board:
    title: str
    """제목"""
    articles: list[Article]
    """게시글"""
