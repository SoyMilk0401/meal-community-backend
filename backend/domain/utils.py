from datetime import datetime
from typing import Any


def dict_factory(data: list[tuple[str, Any]]):
    return {k: v.isoformat() if isinstance(v, datetime) else v for k, v in data}
