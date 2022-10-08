from typing import Optional

from fastapi import APIRouter, Depends, status
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate

from app import schemes
from app.services.auth import get_current_user
from app.services.trend import TrendService

router = APIRouter(
    prefix="/trend",
    tags=["trend"],
)


@router.get(
    "/",
    response_model=Page[schemes.TrendWithFavoriteORM],
)
def get_trends(
    favorite: Optional[bool] = None,
    exclude_ids: Optional[str] = None,
    trend_service: TrendService = Depends(),
    user=Depends(get_current_user),
):
    return paginate(trend_service.filter_all(user, favorite, exclude_ids))


@router.post(
    "/{trend_id}/favorite/",
    status_code=status.HTTP_200_OK,
)
def favorite_trends(
    trend_id: int,
    trend_service: TrendService = Depends(),
    user=Depends(get_current_user),
):
    return trend_service.add_or_remove_favorite(trend_id, user)
