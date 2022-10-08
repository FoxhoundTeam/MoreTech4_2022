from typing import Type, TypeVar, cast

from fastapi import HTTPException
from sqlalchemy.orm.session import Session
from starlette import status

from app.database import Base

T = TypeVar("T")


def get_or_404(session: Session, model: Type[Base], _id: int):
    obj = session.query(model).get(_id)
    if obj is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Entity with such id doesn't exist",
        )
    return cast(type(model), obj)
