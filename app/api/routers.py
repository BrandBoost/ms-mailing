from fastapi import APIRouter

from app.api.v1.gmail import api_router as gmail_api_router
from app.api.v1.whatsapp import api_router as whatsapp_api_router


v1_router = APIRouter(prefix='/api/v1/mailing')

v1_router.include_router(gmail_api_router, prefix="/gmail", tags=["mails"])
v1_router.include_router(whatsapp_api_router, prefix="/whatsapp", tags=["mails"])
