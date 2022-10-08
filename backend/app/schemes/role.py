from .base import CamelModel


class Role(CamelModel):
    name: str
    code: int


class RoleORM(Role):
    id: int

    class Config:
        orm_mode = True
