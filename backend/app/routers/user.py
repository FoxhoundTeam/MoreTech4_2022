from fastapi import APIRouter, Depends

from app import schemes
from app.services.auth import get_current_user
from app.services.user import UserService

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get(
    "/user/",
    response_model=schemes.UserORM,
)
def get_user(user: schemes.UserORM = Depends(get_current_user)):
    return user


@router.patch(
    "/user/",
    response_model=schemes.UserORM,
)
def patch_user(data: schemes.UserPatch, user_service: UserService = Depends(), user=Depends(get_current_user)):
    return user_service.patch_user(user, data)
