from typing import Optional

from .base import CamelModel


class TrendLink(CamelModel):
    link: str
    site_name: str
    header: Optional[str]
    image_link: Optional[str]


class TrendLinkORM(TrendLink):
    id: int

    class Config:
        orm_mode = True
