from twilio.rest import Client
from twilio.twiml.voice_response import Play
from twilio.twiml.voice_response import VoiceResponse

from app.config import settings

client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)


async def call_test(phone_number: str, text: str):
    response = VoiceResponse()
    audio = Play(url='https://mp3uk.net/mp3/files/bushido-zho-green-orxnge-vodila-phonk-remix-mp3.mp3')
    response.say(text)
    response.append(audio)
    client.calls.create(
        twiml=response,
        to=phone_number,
        from_=settings.TWILIO_PHONE_NUMBER
    )
