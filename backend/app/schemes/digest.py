from typing import Optional
from pydantic import Field

from .base import CamelModel


class Digest(CamelModel):
    title: str
    topic: list[str] = Field(default_factory=[])
    image_tags: Optional[str]


class DigestORM(Digest):
    id: int

    class Config:
        orm_mode = True
