import logging
import os

from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger()
logging.basicConfig(
    level=logging.DEBUG, format='%(asctime)s: %(levelname)s: %(message)s'
)

# FastAPI configuration
HOST = os.getenv('FASTAPI_HOST', '0.0.0.0')
PORT = os.getenv('FASTAPI_PORT', '8000')

# MongoDB
MONGO_URI = os.getenv('MONGO_URI')
DB_NAME = os.getenv('DB_NAME')

# Twilio settings
TWILIO_ACCOUNT_SID = os.getenv('ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')
TWILIO_WHATSAPP_PHONE_NUMBER = os.getenv('TWILIO_WHATSAPP_PHONE_NUMBER')

# Gmail settings
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

# Token configuration
SECRET_KEY = os.getenv('SECRET_KEY')
JWT_ALGORITHM = os.getenv('JWT_ALGORITHM')
JWT_ACCESS_TTL = int(os.environ.get('JWT_ACCESS_TTL', 50))
JWT_REFRESH_TTL = int(os.environ.get('JWT_REFRESH_TTL', 500))
REFRESH_TOKEN_JWT_SUBJECT = 'refresh'
ACCESS_TOKEN_JWT_SUBJECT = 'access'
TOKEN_TYPE = "Bearer"

# CORS
URL_LOCALHOST_FRONT = os.getenv("URL_LOCALHOST_FRONT", '')
URL_BRENDBOOST_BACK = os.getenv("URL_BRENDBOOST_BACK", '')
URL_BRENDBOOST_FRONT = os.getenv("URL_BRENDBOOST_FRONT", '')
