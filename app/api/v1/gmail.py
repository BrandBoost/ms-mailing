from fastapi import APIRouter

from app.schemas.emails import EmailSchema
from app.services import gmail

api_router = APIRouter()


@api_router.post('/send_multi_email_advertising', status_code=200)
async def send_ads_by_email(data: EmailSchema):
    return await gmail.send_mail(emails=data.emails, content=data.text)
