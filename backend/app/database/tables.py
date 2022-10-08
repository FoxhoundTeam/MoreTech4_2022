import datetime
from typing import Optional

from sqlalchemy import ARRAY, CheckConstraint, Column, Date, ForeignKey, Integer, String, Table, Text
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy.orm import query_expression, relationship

from .base import Base

role_interesting_trend = Table(
    "role_interesting_trend",
    Base.metadata,
    Column("role_id", Integer, ForeignKey("role.id"), primary_key=True),
    Column("interesting_trend_id", Integer, ForeignKey("interestingtrend.id"), primary_key=True),
)

user_trend = Table(
    "user_trend",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("user.id"), primary_key=True),
    Column("trend_id", Integer, ForeignKey("trend.id"), primary_key=True),
)
user_interesting_trend = Table(
    "user_interesting_trend",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("user.id"), primary_key=True),
    Column("interesting_trend_id", Integer, ForeignKey("interestingtrend.id"), primary_key=True),
)


class Trend(Base):
    name: str = Column(String)
    date: datetime.datetime = Column(Date)
    links: list["TrendLink"] = relationship("TrendLink", back_populates="trend", lazy="joined")
    users: list["User"] = relationship("User", secondary=user_trend, back_populates="trends")

    favorite = query_expression()


class TrendLink(Base):
    link: str = Column(String)
    site_name: str = Column(String)
    text: str = Column(Text, default="")
    header: Optional[str] = Column(String, nullable=True, default=None)
    image_link: Optional[str] = Column(String, nullable=True, default=None)

    trend_id: int = Column(Integer, ForeignKey("trend.id"))
    trend: "Trend" = relationship("Trend", back_populates="links")


class InterestingTrend(Base):
    name: str = Column(String)
    roles: list["Role"] = relationship("Role", secondary=role_interesting_trend, back_populates="interesting_trends")
    users: list["User"] = relationship("User", secondary=user_interesting_trend, back_populates="interesting_trends")


class Role(Base):
    name: str = Column(String)
    code: int = Column(Integer)
    interesting_trends: list["Trend"] = relationship(
        "InterestingTrend",
        secondary=role_interesting_trend,
        back_populates="roles",
    )


class User(Base):
    email: str = Column(String, unique=True)
    password_hash: str = Column(String)
    keywords: list[str] = Column(MutableList.as_mutable(ARRAY(String)), nullable=False, default=[])
    relevant_trends_count = Column(Integer, default=3, nullable=False)
    interesting_trends: list["InterestingTrend"] = relationship(
        "InterestingTrend", secondary=user_interesting_trend, back_populates="users", lazy="joined"
    )
    trends: list["Trend"] = relationship("Trend", secondary=user_trend, back_populates="users")
    __table_args__ = (
        CheckConstraint("relevant_trends_count > 0", name="min_relevant_trends_count"),
        CheckConstraint("relevant_trends_count <= 10", name="max_relevant_trends_count"),
    )
