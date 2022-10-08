from app import database
from app.services.base import BaseDBService


class InterestingTrendService(BaseDBService):
    def get_all(self) -> list[database.InterestingTrend]:
        return self.session.query(database.InterestingTrend).all()
