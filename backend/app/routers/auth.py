from fastapi import APIRouter, Depends, status

from app import database, schemes
from app.services.auth import AuthService, get_current_user

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post(
    "/sign-up/",
    response_model=schemes.Token,
    status_code=status.HTTP_201_CREATED,
)
def sign_up(
    user_data: schemes.UserCreate,
    auth_service: AuthService = Depends(),
):
    return auth_service.register_new_user(user_data)


@router.post(
    "/sign-in/",
    response_model=schemes.Token,
)
def sign_in(
    auth_data: schemes.Credentials,
    auth_service: AuthService = Depends(),
):
    return auth_service.authenticate_user(auth_data.email, auth_data.password)


@router.post(
    "/change-password/",
    status_code=status.HTTP_200_OK,
)
def change_password(
    data: schemes.ChangePassword,
    auth_service: AuthService = Depends(),
    user: database.User = Depends(get_current_user),
):
    auth_service.change_password(data, user)
