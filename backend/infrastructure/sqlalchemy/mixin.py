from dataclasses import dataclass

from sqlalchemy.orm import Mapped, mapped_column


@dataclass(kw_only=True)
class Schema:
    """
    스키마의 기본 클래스입니다.

    모든 스키마는 이 클래스를 상속받습니다.
    """

    id: Mapped[int] = mapped_column(default=None, kw_only=True, primary_key=True)
