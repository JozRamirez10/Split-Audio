from app.core.constants import DRUMS_NAME, DRUMS_MODEL
from app.enums.drum_instruments import DrumInstruments
from app.services.split_local_service import SplitLocalService

drum_service = SplitLocalService(
    service_name=DRUMS_NAME,
    model_filename=DRUMS_MODEL,
    enum_class=DrumInstruments
)