
from fastapi import APIRouter

from app.schemas.whatsapp import WhatsappSchema
from app.services import whatsapp

api_router = APIRouter()


@api_router.post('/send_whatsapp_advertising', status_code=200)
async def send_ads_by_whatsapp(data: WhatsappSchema):
    return await whatsapp.send_messages(whatsapp_numbers=data.phones, text=data.text)
