from app import database
from app.services.trend import TrendService


class RelevantTrendService(TrendService):
    def get_all(self, user: database.User) -> list[database.Trend]:
        # TODO
        return self._get_all_query(user)[0].limit(user.relevant_trends_count).all()
