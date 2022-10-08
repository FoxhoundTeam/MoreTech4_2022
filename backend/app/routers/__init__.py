from fastapi import APIRouter

from . import auth, digest, interesting_theme, roles, trend, user

router = APIRouter(prefix="/api")
router.include_router(auth.router)
router.include_router(user.router)
router.include_router(roles.router)
router.include_router(interesting_theme.router)
router.include_router(trend.router)
router.include_router(digest.router)
