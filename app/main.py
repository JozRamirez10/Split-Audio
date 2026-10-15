import logging
from fastapi import FastAPI
import uvicorn

from app.core.constants import FORMAT_LOG

logging.basicConfig(
    level=logging.INFO,
    format=FORMAT_LOG
)

from app.controllers.split_audio_controller import router as audio_router

app = FastAPI(title="Split Audio API", version="1.0.0")

app.include_router(audio_router)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=7002)