from typing import Optional

from sqlalchemy import and_, exists
from sqlalchemy.orm import Query, with_expression
from sqlalchemy.sql.elements import UnaryExpression

from app import database
from app.services.base import BaseDBService


class TrendService(BaseDBService):
    def _get_all_query(self, user: database.User) -> tuple[Query, UnaryExpression]:
        favorite_expr = exists().where(
            database.user_trend.c.trend_id == database.Trend.id,
            database.user_trend.c.user_id == user.id,
        )
        return (
            self.session.query(database.Trend).options(
                with_expression(
                    database.Trend.favorite,
                    favorite_expr,
                )
            ),
            favorite_expr,
        )

    def filter_all(self, user: database.User, favorite: Optional[bool], day: Optional[int]) -> Query:
        query, favorite_expr = self._get_all_query(user)
        if favorite is not None:
            query = query.filter(favorite_expr.is_(favorite))
        return query

    def add_or_remove_favorite(self, trend_id: int, user: database.User):
        exists_query = self.session.query(database.user_trend).filter(
            database.user_trend.c.user_id == user.id,
            database.user_trend.c.trend_id == trend_id,
        )
        is_exists = bool(self.session.query(exists_query.exists()).scalar())
        trend = self.session.query(database.Trend).get(trend_id)
        if is_exists:
            user.trends.remove(trend)
        else:
            user.trends.append(trend)

        self.session.add(user)
        self.session.commit()

    def get_news(self, trend_id: int) -> list[database.News]:
        query: Query = self.session.query(database.News)
        return (
            query.join(database.trend_news)
            .join(
                database.Trend,
                and_(
                    database.trend_news.c.trend_id == database.Trend.id,
                    database.Trend.id == trend_id,
                ),
            )
            .all()
        )
