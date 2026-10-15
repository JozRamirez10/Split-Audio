from typing import List, Optional, TypeVar, Generic
from pydantic import BaseModel
from enum import Enum

T = TypeVar("T", bound=Enum)

class SeparationRequest(BaseModel, Generic[T]):
    input_path: str
    desired_tracks: Optional[List[T]] = []

class SeparationResponse(BaseModel):
    input_path: str
    output_paths: List[str]