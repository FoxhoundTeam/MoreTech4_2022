from sqlalchemy import and_
from sqlalchemy.orm import Query

from app import database

from .base import BaseDBService


class DigestService(BaseDBService):
    def get_all(self, user: database.User) -> list[database.Digest]:
        return self.session.query(database.Digest).filter(database.Digest.user_id == user.id).all()

    def get_news(self, digest_id: int) -> list[database.News]:
        query: Query = self.session.query(database.News)
        return (
            query.join(database.digest_news)
            .join(
                database.Digest,
                and_(
                    database.digest_news.c.digest_id == database.Digest.id,
                    database.Digest.id == digest_id,
                ),
            )
            .all()
        )
