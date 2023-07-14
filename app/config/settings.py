import logging
import os

logger = logging.getLogger()
logging.basicConfig(
    level=logging.DEBUG, format='%(asctime)s: %(levelname)s: %(message)s'
)

# FastAPI configuration
HOST = os.getenv('FASTAPI_HOST', '0.0.0.0')
PORT = os.getenv('FASTAPI_PORT', '8000')

TWILIO_ACCOUNT_SID = os.getenv('ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')
TWILIO_WHATSAPP_PHONE_NUMBER = os.getenv('TWILIO_WHATSAPP_PHONE_NUMBER')

EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
