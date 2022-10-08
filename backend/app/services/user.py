from app import database, schemes
from app.services.base import BaseDBService


class UserService(BaseDBService):
    def get_by_id(self, _id: int) -> database.User:
        return self.session.query(database.User).get(_id)

    def patch_user(self, user: database.User, patch_data: schemes.UserPatch):
        if patch_data.dict(include={"keywords", "interesting_themes", "relevant_digests_count"}, exclude_none=True):
            user.digests.clear()
        for key, value in patch_data.dict(exclude_none=True, exclude={"interesting_themes"}).items():
            setattr(user, key, value)
        if (its := patch_data.interesting_themes) is not None:
            user.interesting_trends = (
                self.session.query(database.InterestingTheme)
                .filter(database.InterestingTheme.id.in_([it.id for it in its]))
                .all()
            )
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user
