from app.core.constants import GUITAR_ROLE_NAME, GUITAR_ROLE_WORKFLOW
from app.services.split_cloud_service import SplitCloudService
from app.enums.guitar_instruments import GuitarRoleInstruments

guitar_role_service = SplitCloudService(
    service_name=GUITAR_ROLE_NAME,
    workflow_slug=GUITAR_ROLE_WORKFLOW,
    enum_class=GuitarRoleInstruments
)