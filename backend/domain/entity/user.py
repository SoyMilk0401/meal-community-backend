from dataclasses import dataclass
from datetime import datetime

from backend.domain.entity.school_info import SchoolInfo


@dataclass
class User:
    name: str
    """이름"""
    email: str
    """이메일"""
    password: str
    """비밀번호"""
    school_info: SchoolInfo
    """학교 정보"""
    created_at: datetime
    """생성일"""
