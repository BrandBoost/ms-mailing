from twilio.rest import Client

from app.config import settings


async def send_messages(whatsapp_numbers: list, text: str):
    # Create a Twilio client
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)  # type: ignore

    # Send a message
    phone_numbers = map(lambda number: f'whatsapp:{number}', whatsapp_numbers)
    client.messages.create(
        body=text,
        from_=settings.TWILIO_WHATSAPP_PHONE_NUMBER,  # type: ignore
        to=list(phone_numbers)
    )
