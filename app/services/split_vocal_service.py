from app.core.constants import VOCAL_MODEL, VOCAL_NAME
from app.enums.vocal_instruments import VocalInstruments
from app.services.split_local_service import SplitLocalService

vocal_service = SplitLocalService(
    service_name=VOCAL_NAME,
    model_filename=VOCAL_MODEL,
    enum_class=VocalInstruments
)