import mimetypes
import os
import uuid

from typing import List
from bson import ObjectId
from fastapi import HTTPException
from fastapi import UploadFile


from app.config import settings


async def save_file_to_project(user_id: str, file: UploadFile):
    try:
        media_path = os.path.join("media", "userdata", "audio")
        if not os.path.exists(media_path):
            os.makedirs(media_path)

        unique_filename = str(uuid.uuid4()).replace('-', '')

        content_type, _ = mimetypes.guess_type(str(file.filename))
        if content_type is None or not content_type.startswith("audio"):
            file_extension = "mp3"
        else:
            file_extension = str(mimetypes.guess_extension(content_type))
            if file_extension:
                file_extension = file_extension[1:]

        file_name = f"{unique_filename}.{file_extension}"
        file_path = os.path.join("media/userdata/audio", file_name)

        with open(file_path, "wb") as f:
            f.write(file.file.read())

        file_path = file_path.replace("\\", "/")

        # await UsersRepository().update_by_id(
        #     ObjectId(user_id), {"avatar_link": file_path}
        # )
        image_link = f"{settings.SERVICE_URL}/{file_path}/"
        return {"audio_link": image_link}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
