import logging
from fastapi import HTTPException

logger = logging.getLogger(__name__)

def error_handler_api(e: Exception, context: str):
    if isinstance(e, ValueError):
        return HTTPException(status_code=400, detail=str(e))
    elif isinstance(e, PermissionError):
        return HTTPException(status_code=403, detail=str(e))
    elif isinstance(e, FileNotFoundError):
        return HTTPException(status_code=404, detail=str(e))
    else:
        logger.error(f"Unhandled exception during {context}: {str(e)}")
        return HTTPException(status_code=500, detail=f"Internal server error during {context}")