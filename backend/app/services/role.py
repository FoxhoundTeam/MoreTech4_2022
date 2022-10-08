from app import database
from app.services.base import BaseDBService


class RoleService(BaseDBService):
    def get_all(self) -> list[database.Role]:
        return self.session.query(database.Role).all()
