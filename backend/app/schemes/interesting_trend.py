from .base import CamelModel


class InterestingTrend(CamelModel):
    name: str


class InterestingTrendORM(InterestingTrend):
    id: int

    class Config:
        orm_mode = True
