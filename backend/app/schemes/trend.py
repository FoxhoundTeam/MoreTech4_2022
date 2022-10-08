import datetime

from .base import CamelModel
from .trend_link import TrendLinkORM


class Trend(CamelModel):
    name: str
    date: datetime.date
    links: list[TrendLinkORM]


class TrendORM(Trend):
    id: int

    class Config:
        orm_mode = True


class TrendWithFavoriteORM(TrendORM):
    favorite: bool
