from fastapi import APIRouter, Depends

from app import schemes
from app.services.role import RoleService

router = APIRouter(
    prefix="/roles",
    tags=["roles"],
)


@router.get(
    "/",
    response_model=list[schemes.RoleORM],
)
def get_roles(role_service: RoleService = Depends()):
    return role_service.get_all()
