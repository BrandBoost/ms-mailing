from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import v1_router
from app.config import logger

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000', 'https://brandboost-demo.web.app', 'https://auth-and-login-app.herokuapp.com'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def on_startup():
    logger.info('Startup event - connecting to the database')


app.include_router(v1_router)
