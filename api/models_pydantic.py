from typing import Tuple

from pydantic import BaseModel


class User(BaseModel):
    """Модель данных json."""
    name: str | None = None
    photo_url: str | None = None
    description: str | None = None
    location: Tuple[float, float] | None = None
