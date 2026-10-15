import os
import logging
from abc import ABC, abstractmethod

from app.core.config import TMP_DIR
from app.core.constants import ALLOWED_AUDIO_EXTENSIONS, MAX_FILE_SIZE_MB

FILE_NOT_FOUND = "File not found"
BAD_REQUEST_EXT = "Invalid file extension"
BAD_REQUEST_SIZE = "File size exceeds maximum allowed"
SECURITY_ERROR = "Path traversal attempt blocked for path"

logger = logging.getLogger(__name__)

class SplitBaseService(ABC):

    def __init__(self, service_name: str, enum_class):
        self.enum_class = enum_class
        logger.info(f"*** {service_name} initialized")

    def separate(self, input_path: str, desired_tracks: list) -> list[str]:
        abs_path = self._validate_input_file(input_path)

        base_name = os.path.splitext(os.path.basename(abs_path))[0]
        output_dir = os.path.join(TMP_DIR, base_name)
        os.makedirs(output_dir, exist_ok=True)

        tracks_to_keep = [track.value.lower() for track in desired_tracks] if desired_tracks else [t.value.lower() for t in self.enum_class]

        logger.info(f"*** Starting separation process for {base_name}...")
        return self._perform_separation(abs_path, base_name, output_dir, tracks_to_keep)

    @abstractmethod
    def _perform_separation(self, abs_path: str, base_name: str, output_dir: str, tracks_to_keep: list) -> list[str]:
        """It must be implemented by the child classes"""
        pass

    def _validate_input_file(self, input_path: str) -> str:

        abs_path = os.path.abspath(input_path)
        if not abs_path.startswith(TMP_DIR):
            raise PermissionError(f"{SECURITY_ERROR}: {input_path}")

        _, ext = os.path.splitext(abs_path)
        if ext.lower() not in ALLOWED_AUDIO_EXTENSIONS:
            raise ValueError(f"{BAD_REQUEST_EXT}: {ext}. Allowed: {ALLOWED_AUDIO_EXTENSIONS}")

        if not os.path.exists(abs_path):
            raise FileNotFoundError(f"{FILE_NOT_FOUND}: {input_path}")

        size_mb = os.path.getsize(abs_path) / (1024 * 1024)
        if size_mb > MAX_FILE_SIZE_MB:
            raise ValueError(f"{BAD_REQUEST_SIZE}: {size_mb:.2f} MB. Max {MAX_FILE_SIZE_MB} MB")

        return abs_path