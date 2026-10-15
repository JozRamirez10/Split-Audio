import logging
from fastapi import APIRouter

from app.models.payload import SeparationRequest, SeparationResponse
from app.models.cleanup_payload import CleanupRequest, CleanupResponse

from app.enums.track_instruments import TrackInstruments
from app.enums.drum_instruments import DrumInstruments
from app.enums.vocal_instruments import VocalInstruments
from app.enums.winds_instruments import WindsInstruments
from app.enums.guitar_instruments import GuitarRoleInstruments, GuitarTypeInstruments

from app.services.split_base_service import SplitBaseService
from app.services.split_audio_service import track_service
from app.services.split_drums_service import drum_service
from app.services.split_vocal_service import vocal_service
from app.services.split_winds_service import wind_service
from app.services.split_guitar_role_musicai_service import guitar_role_service
from app.services.split_guitar_type_musicai_service import guitar_type_service

from app.services.cleanup_service import cleanup_service

from app.utils.error_handler import error_handler_api

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api")

@router.post("/process-tracks", response_model=SeparationResponse)
def process_tracks(payload: SeparationRequest[TrackInstruments]):
    return _execute_separation(payload, track_service, "tracks")

@router.post("/process-drums", response_model=SeparationResponse)
def process_drums(payload: SeparationRequest[DrumInstruments]):
    return _execute_separation(payload, drum_service, "drums")

@router.post("/process-vocals", response_model=SeparationResponse)
def process_vocals(payload: SeparationRequest[VocalInstruments]):
    return _execute_separation(payload, vocal_service, "vocals")

@router.post("/process-winds", response_model=SeparationResponse)
def process_winds(payload: SeparationRequest[WindsInstruments]):
    return _execute_separation(payload, wind_service, "winds")

@router.post("/process-role-guitars", response_model=SeparationResponse)
def process_role_guitars(payload: SeparationRequest[GuitarRoleInstruments]):
    return _execute_separation(payload, guitar_role_service, "role guitars")

@router.post("/process-type-guitars", response_model=SeparationResponse)
def process_type_guitars(payload: SeparationRequest[GuitarTypeInstruments]):
    return _execute_separation(payload, guitar_type_service, "type guitars")

@router.delete("/cleanup", response_model=CleanupResponse)
def cleanup_temp_folder(payload: CleanupRequest):

    logger.info(f"*** Received cleanup request for: {payload.target_path}")

    try:
        path_deleted = cleanup_service.cleanup_path(payload.target_path)
        if path_deleted:
            return CleanupResponse(
                path_deleted=path_deleted
            )
        else:
            raise FileNotFoundError(f"Path does not exist: {payload.target_path}")

    except Exception as e:
        raise error_handler_api(e, "folder cleanup")

def _execute_separation(payload: SeparationRequest, service: SplitBaseService, context_name: str) -> SeparationResponse:

    logger.info(f"*** Received {context_name} separation request for: {payload.input_path}")

    try:
        output_paths = service.separate(
            input_path=payload.input_path,
            desired_tracks=payload.desired_tracks or []
        )

        return SeparationResponse(
            input_path=payload.input_path,
            output_paths=output_paths
        )

    except Exception as e:
        raise error_handler_api(e, context_name)
