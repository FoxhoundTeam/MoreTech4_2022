from typing import Optional

from pydantic import EmailStr, conint

from .base import CamelModel
from .interesting_trend import InterestingTrendORM


class BaseUser(CamelModel):
    email: EmailStr
    relevant_trends_count: conint(gt=0, le=10) = 3


class UserCreate(BaseUser):
    password: str
    role: Optional[int] = None


class UserPatch(CamelModel):
    email: Optional[EmailStr] = None
    relevant_trends_count: Optional[conint(gt=0, le=10)] = None
    interesting_trends: Optional[list[InterestingTrendORM]] = None
    keywords: Optional[list[str]] = None


class UserORM(BaseUser):
    id: int
    interesting_trends: list[InterestingTrendORM]
    keywords: list[str]

    class Config:
        orm_mode = True
