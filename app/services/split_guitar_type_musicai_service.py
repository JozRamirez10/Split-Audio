from app.core.constants import GUITAR_TYPE_NAME, GUITAR_TYPE_WORKFLOW
from app.enums.guitar_instruments import GuitarTypeInstruments
from app.services.split_cloud_service import SplitCloudService

guitar_type_service = SplitCloudService(
    service_name=GUITAR_TYPE_NAME,
    workflow_slug=GUITAR_TYPE_WORKFLOW,
    enum_class=GuitarTypeInstruments
)