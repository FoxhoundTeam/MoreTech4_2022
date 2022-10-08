from typing import Optional

from pydantic import EmailStr, conint

from .base import CamelModel
from .interesting_theme import InterestingThemeORM


class BaseUser(CamelModel):
    email: EmailStr
    relevant_digests_count: conint(gt=0, le=10) = 3


class UserCreate(BaseUser):
    password: str
    role: Optional[int] = None


class UserPatch(CamelModel):
    email: Optional[EmailStr] = None
    relevant_digests_count: Optional[conint(gt=0, le=10)] = None
    interesting_themes: Optional[list[InterestingThemeORM]] = None
    keywords: Optional[list[str]] = None


class UserORM(BaseUser):
    id: int
    interesting_themes: list[InterestingThemeORM]
    keywords: list[str]

    class Config:
        orm_mode = True
