import os

from fastapi import APIRouter, Request, UploadFile, HTTPException
from fastapi.responses import FileResponse

from app.schemas.audio_file import AudioMessageSchema
from app.services.audio_file import save_file_to_project

api_router = APIRouter()


@api_router.post("/me/audio/", status_code=200, response_model=AudioMessageSchema)
async def send_ads_by_email(request: Request, file: UploadFile):
    user_id = request.state.user_id
    return await save_file_to_project(user_id=user_id, file=file)


@api_router.get('/userdata/audio/{file_name}/')
async def get_media(file_name: str):

    file_path = os.path.join("media/userdata/audio", file_name)
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type="audio/mp3")
    else:
        raise HTTPException(status_code=404, detail="File not found")
