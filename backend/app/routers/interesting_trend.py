from fastapi import APIRouter, Depends

from app import schemes
from app.services.interesting_trend import InterestingTrendService

router = APIRouter(
    prefix="/interesting-trend",
    tags=["interesting-trend"],
)


@router.get(
    "/",
    response_model=list[schemes.InterestingTrendORM],
)
def get_interesting_trends(interesting_trend_service: InterestingTrendService = Depends()):
    return interesting_trend_service.get_all()
