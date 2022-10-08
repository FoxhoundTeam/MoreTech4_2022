from fastapi import APIRouter, Depends

from app import schemes
from app.services.auth import get_current_user
from app.services.digest import DigestService

router = APIRouter(
    prefix="/digest",
    tags=["digest"],
)


@router.get(
    "/",
    response_model=list[schemes.DigestORM],
)
def get_relevant_trends(
    digest_service: DigestService = Depends(),
    user=Depends(get_current_user),
):
    # TODO
    return digest_service.get_all(user)


@router.get(
    "/{digest_id}/news/",
    response_model=list[schemes.NewsORM],
)
def digest_news(
    digest_id: int,
    digest_service: DigestService = Depends(),
):
    return digest_service.get_news(digest_id)
