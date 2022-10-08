from app import database
from app.services.base import BaseDBService


class InterestingThemeService(BaseDBService):
    def get_all(self) -> list[database.InterestingTheme]:
        return self.session.query(database.InterestingTheme).all()
