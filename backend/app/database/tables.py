import datetime
from typing import Optional

from sqlalchemy import ARRAY, CheckConstraint, Column, Date, ForeignKey, Integer, String, Table, Text
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy.orm import query_expression, relationship

from .base import Base

role_interesting_theme = Table(
    "role_interesting_theme",
    Base.metadata,
    Column("role_id", Integer, ForeignKey("role.id"), primary_key=True),
    Column("interesting_theme_id", Integer, ForeignKey("interestingtheme.id"), primary_key=True),
)

user_trend = Table(
    "user_trend",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("user.id"), primary_key=True),
    Column("trend_id", Integer, ForeignKey("trend.id"), primary_key=True),
)
user_interesting_theme = Table(
    "user_interesting_trend",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("user.id"), primary_key=True),
    Column("interesting_theme_id", Integer, ForeignKey("interestingtheme.id"), primary_key=True),
)

digest_news = Table(
    "digest_news",
    Base.metadata,
    Column("digest_id", Integer, ForeignKey("digest.id", ondelete="CASCADE"), primary_key=True),
    Column("news_id", Integer, ForeignKey("news.id", ondelete="CASCADE"), primary_key=True),
)

trend_news = Table(
    "trend_news",
    Base.metadata,
    Column("trend_id", Integer, ForeignKey("trend.id"), primary_key=True),
    Column("news_id", Integer, ForeignKey("news.id"), primary_key=True),
)


class Trend(Base):
    title: str = Column(String, nullable=False)
    topic: list[str] = Column(ARRAY(String), nullable=False, default=[])
    date: datetime.date = Column(Date, nullable=False)
    users: list["User"] = relationship("User", secondary=user_trend, back_populates="trends")
    news: list["News"] = relationship("News", secondary=trend_news, back_populates="trends")

    favorite = query_expression()


class News(Base):
    title: str = Column(String, nullable=False)
    url: str = Column(String, nullable=False)
    text: str = Column(Text, nullable=False)
    date: datetime.date = Column(Date, nullable=False)
    url_preview: Optional[str] = Column(String, nullable=True, default=None)
    text_prepared: list[str] = Column(ARRAY(String), nullable=False, default=[])
    title_prepared: list[str] = Column(ARRAY(String), nullable=False, default=[])

    digests: list["Digest"] = relationship("Digest", secondary=digest_news, back_populates="news", passive_deletes=True)
    trends: list["Trend"] = relationship("Trend", secondary=trend_news, back_populates="news")


class InterestingTheme(Base):
    name: str = Column(String, nullable=False)
    roles: list["Role"] = relationship("Role", secondary=role_interesting_theme, back_populates="interesting_themes")
    users: list["User"] = relationship("User", secondary=user_interesting_theme, back_populates="interesting_themes")


class Digest(Base):
    title: str = Column(String, nullable=False)
    topic: list[str] = Column(ARRAY(String), nullable=False, default=[])
    user_id: int = Column(Integer, ForeignKey("user.id"))
    user: "User" = relationship("User", back_populates="digests")
    news: list["News"] = relationship("News", secondary=digest_news, back_populates="digests", passive_deletes=True)


class Role(Base):
    name: str = Column(String)
    code: int = Column(Integer)
    interesting_themes: list["InterestingTheme"] = relationship(
        "InterestingTheme",
        secondary=role_interesting_theme,
        back_populates="roles",
    )


class User(Base):
    email: str = Column(String, unique=True)
    password_hash: str = Column(String)
    keywords: list[str] = Column(MutableList.as_mutable(ARRAY(String)), nullable=False, default=[])
    relevant_digests_count = Column(Integer, default=3, nullable=False)
    interesting_themes: list["InterestingTheme"] = relationship(
        "InterestingTheme", secondary=user_interesting_theme, back_populates="users", lazy="joined"
    )
    trends: list["Trend"] = relationship("Trend", secondary=user_trend, back_populates="users")
    digests: list["Digest"] = relationship("Digest", back_populates="user")
    __table_args__ = (
        CheckConstraint("relevant_digests_count > 0", name="min_relevant_digests_count"),
        CheckConstraint("relevant_digests_count <= 10", name="max_relevant_digests_count"),
    )
