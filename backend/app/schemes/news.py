import datetime
from typing import Optional

from .base import CamelModel


class News(CamelModel):
    title: str
    url: str
    text: str
    date: datetime.date
    url_preview: Optional[str]


class NewsORM(News):
    id: int

    class Config:
        orm_mode = True
