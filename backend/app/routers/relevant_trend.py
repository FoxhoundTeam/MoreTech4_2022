from fastapi import APIRouter, Depends

from app import schemes
from app.services.auth import get_current_user
from app.services.relevant_trend import RelevantTrendService

router = APIRouter(
    prefix="/relevant-trend",
    tags=["relevant-trend"],
)


@router.get(
    "/",
    response_model=list[schemes.TrendWithFavoriteORM],
)
def get_relevant_trends(
    relevant_trend_service: RelevantTrendService = Depends(),
    user=Depends(get_current_user),
):
    # TODO
    return relevant_trend_service.get_all(user)
