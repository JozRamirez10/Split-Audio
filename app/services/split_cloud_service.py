import os
import json
import logging
from musicai_sdk import MusicAiClient

from app.services.split_base_service import SplitBaseService
from app.core.config import MUSIC_AI_API_KEY

logger = logging.getLogger(__name__)

class SplitCloudService(SplitBaseService):

    def __init__(self, service_name: str, workflow_slug: str, enum_class):
        super().__init__(service_name, enum_class)
        self.workflow_slug = workflow_slug
        self.client = MusicAiClient(api_key=MUSIC_AI_API_KEY)

    def _perform_separation(self, abs_path: str, base_name: str, output_dir: str, tracks_to_keep: list) -> list[str]:
        song_url = self.client.upload_file(abs_path)
        logger.info(f"*** Music.AI Upload URL generated: {song_url}")

        job_data = self.client.add_job(
            job_name=f"Job_{base_name}",
            workflow_slug=self.workflow_slug,
            params={"inputGuitar": song_url}
        )
        job_id = job_data["id"]

        try:
            completed_job = self.client.wait_for_job_completion(job_id)
            if completed_job["status"] != "SUCCEEDED":
                raise Exception(f"Music.AI job failed: {completed_job.get('error')}")

            self.client.download_job_results(completed_job, output_dir)
            final_files = []

            results_json_path = os.path.join(output_dir, "workflow.result.json")
            if os.path.exists(results_json_path):
                with open(results_json_path, "r") as f:
                    results_data = json.load(f)

                logger.info(f"*** Music.AI returned keys: {list(results_data.keys())}")
                logger.info(f"*** We are looking for: {tracks_to_keep}")

                for output_key, rel_path in results_data.items():
                    if not isinstance(rel_path, str):
                        continue

                    clean_output_key = output_key.lower().strip()

                    for track in tracks_to_keep:
                        if track in clean_output_key or clean_output_key in track:
                            original_path = os.path.normpath(os.path.join(output_dir, rel_path))

                            if not original_path.startswith(output_dir):
                                continue

                            if os.path.exists(original_path):
                                _, ext = os.path.splitext(original_path)
                                new_name = f"{base_name}_{track}{ext}"
                                new_path = os.path.join(output_dir, new_name)

                                os.rename(original_path, new_path)
                                final_files.append(new_path)
                                logger.info(f"*** Kept and renamed: {new_path}")
                            break

                for filename in os.listdir(output_dir):
                    file_path = os.path.join(output_dir, filename)
                    if file_path not in final_files and not filename.endswith(".json"):
                        os.remove(file_path)
                        logger.info(f"*** Deleted unwanted file: {file_path}")

            return final_files

        finally:
            self.client.delete_job(job_id)
