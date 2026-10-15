from app.core.constants import TRACK_MODEL, TRACK_NAME
from app.enums.track_instruments import TrackInstruments
from app.services.split_local_service import SplitLocalService

track_service = SplitLocalService(
    service_name=TRACK_NAME,
    model_filename=TRACK_MODEL,
    enum_class=TrackInstruments
)