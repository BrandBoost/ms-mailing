from fastapi import APIRouter

from app.api.v1.gmail import api_router as gmail_api_router
from app.api.v1.whatsapp import api_router as whatsapp_api_router
from app.api.v1.bases import api_router as bases_api_router


v1_router = APIRouter(prefix='/api/v1/mailing')

v1_router.include_router(gmail_api_router, prefix="/gmail", tags=["emails mailing"])
v1_router.include_router(whatsapp_api_router, prefix="/whatsapp", tags=["phones mailing"])
v1_router.include_router(bases_api_router, prefix="/bases", tags=["bases management"])
