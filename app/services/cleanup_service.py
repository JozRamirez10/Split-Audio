import os
import shutil
import logging
from typing import Optional
from app.core.config import TMP_DIR

logger = logging.getLogger(__name__)

class CleanupService:

    def __init__(self):
        logger.info("*** Cleanup Service initialized")

    def cleanup_path(self, target_path: str) -> Optional[str]:

        abs_path = os.path.abspath(target_path)

        if not abs_path.startswith(TMP_DIR):
            raise PermissionError(f"*** Cannot delete {target_path} directory")

        if os.path.exists(abs_path):

            if os.path.isfile(abs_path):
                os.remove(abs_path)
                logger.info(f"*** Successfully deleted file {abs_path}")
            elif os.path.isdir(abs_path):
                shutil.rmtree(abs_path)
                logger.info(f"*** Successfully deleted folder {abs_path}")

            return target_path
        else:
            logger.info(f"*** Path {target_path} doesn't exist")
            return None

cleanup_service = CleanupService()