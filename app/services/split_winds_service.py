from app.core.constants import WINDS_NAME, WINDS_MODEL
from app.enums.winds_instruments import WindsInstruments
from app.services.split_local_service import SplitLocalService

wind_service = SplitLocalService(
    service_name=WINDS_NAME,
    model_filename=WINDS_MODEL,
    enum_class=WindsInstruments
)