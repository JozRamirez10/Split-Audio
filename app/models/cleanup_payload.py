from pydantic import BaseModel

class CleanupRequest(BaseModel):
    target_path: str

class CleanupResponse(BaseModel):
    path_deleted: str