from .base import CamelModel


class InterestingTheme(CamelModel):
    name: str


class InterestingThemeORM(InterestingTheme):
    id: int

    class Config:
        orm_mode = True
