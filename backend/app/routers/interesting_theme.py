from fastapi import APIRouter, Depends

from app import schemes
from app.services.interesting_theme import InterestingThemeService

router = APIRouter(
    prefix="/interesting-theme",
    tags=["interesting-theme"],
)


@router.get(
    "/",
    response_model=list[schemes.InterestingThemeORM],
)
def get_interesting_trends(interesting_theme_service: InterestingThemeService = Depends()):
    return interesting_theme_service.get_all()
