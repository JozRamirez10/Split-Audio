import os
from dotenv import load_dotenv

load_dotenv()

TMP_DIR = os.getenv("TMP_DIR", "")
MUSIC_AI_API_KEY = os.getenv("MUSIC_AI_API_KEY", "")
DIR_MODELS = os.getenv("DIR_MODELS", "")

if not TMP_DIR:
    raise ValueError("CRITICAL ERROR: TMP_DIR is not defined in the .env file")
if not MUSIC_AI_API_KEY:
    raise ValueError("CRITICAL ERROR: MUSIC_AI_API_KEY is not defined in the .env file")
if not DIR_MODELS:
    raise ValueError("CRITICAL ERROR: DIR_MODELS is not defined in the .env file")