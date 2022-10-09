from sqlalchemy import and_
from sqlalchemy.orm import Query

from app import database
from datetime import date, timedelta

from .base import BaseDBService
import pandas as pd
from app.ml_kernel import extract_digest


class DigestService(BaseDBService):
    def get_all(self, user: database.User) -> list[database.Digest]:
        digests = self.session.query(database.Digest).filter(database.Digest.user_id == user.id).all()
        if not digests:
            return self.generate_digests(user)

    def get_news(self, digest_id: int) -> list[database.News]:
        query: Query = self.session.query(database.News)
        return query.join(
            database.digest_news,
            and_(
                database.News.id == database.digest_news.c.news_id,
                database.digest_news.c.digest_id == digest_id,
            ),
        ).all()

    def generate_digests(self, user: database.User) -> list[database.Digest]:
        news = self.session.query(database.News).filter(database.News.date > date.today() - timedelta(days=14))
        df = pd.read_sql(news.statement, self.session.connection(), index_col="id")
        df["text_prepared2"] = df["text_prepared"]
        df["title_prepared2"] = df["title_prepared"]
        keywords = user.keywords + [theme.name for theme in user.interesting_themes]
        digests = extract_digest(df, keywords)[: user.relevant_digests_count]
        for digest in digests:
            news = self.session.query(database.News).filter(database.News.id.in_(digest.pop("news", [])))
            digest = database.Digest(**digest)
            digest.news = news.all()
            self.session.add(digest)
        self.session.commit()
        return self.session.query(database.Digest).filter(database.Digest.user_id == user.id).all()
