from fastapi import APIRouter

from . import auth, interesting_trend, relevant_trend, roles, trend, user

router = APIRouter(prefix="/api")
router.include_router(auth.router)
router.include_router(user.router)
router.include_router(roles.router)
router.include_router(interesting_trend.router)
router.include_router(trend.router)
router.include_router(relevant_trend.router)
