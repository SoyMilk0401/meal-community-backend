from dataclasses import dataclass


@dataclass
class CreateCommentDTO:
    meal_id: int
    """급식 ID"""
    content: str
    """댓글 내용"""
    parent_id: int | None = None
    """부모 댓글 ID"""
    
@dataclass
class CreateReplyCommentDTO:
    meal_id: int
    """급식 ID"""
    content: str
    """댓글 내용"""
    parent_id: int
    """부모 댓글 ID"""
