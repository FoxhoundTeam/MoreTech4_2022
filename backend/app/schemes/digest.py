from pydantic import Field

from .base import CamelModel


class Digest(CamelModel):
    title: str
    topic: list[str] = Field(default_factory=[])


class DigestORM(Digest):
    id: int

    class Config:
        orm_mode = True
