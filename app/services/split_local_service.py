import os
import threading
import logging
from audio_separator.separator import Separator

from app.services.split_base_service import SplitBaseService
from app.core.config import TMP_DIR
from app.core.config import DIR_MODELS
from app.core.mappings import MODEL_MAPPING

logger = logging.getLogger(__name__)

class SplitLocalService(SplitBaseService):

    def __init__(self, service_name: str, model_filename: str, enum_class):
        super().__init__(service_name, enum_class)

        logger.info(f"*** Loading {model_filename} model in memory...")
        self.separator = Separator(
            output_dir=TMP_DIR,
            model_file_dir=DIR_MODELS
        )
        self.separator.load_model(model_filename=model_filename)
        self.lock = threading.Lock()

    def _perform_separation(self, abs_path: str, base_name: str, output_dir: str, tracks_to_keep: list) -> list[str]:
        with self.lock:
            self.separator.output_dir = output_dir
            output_files = self.separator.separate(abs_path)
            final_files = []

            logger.info("*** Moving and rename stems...")
            for file in output_files:
                original_path = os.path.join(TMP_DIR, file)
                kept = False

                for track in tracks_to_keep:
                    if f"_({track})_" in file.lower():
                        _, ext = os.path.splitext(file)
                        final_track_name = MODEL_MAPPING.get(track, track)
                        new_name = f"{base_name}_{final_track_name}{ext}"
                        new_path = os.path.join(output_dir, new_name)

                        os.rename(original_path, new_path)
                        final_files.append(new_path)
                        kept = True
                        break

                if not kept:
                    os.remove(original_path)

            return final_files