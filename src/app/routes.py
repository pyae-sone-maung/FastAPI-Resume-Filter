from fastapi import APIRouter
import logging

router = APIRouter()
logger = logging.getLogger("main_app_logger")
@router.get("/health")
def health_check():
    logger.info(f"Health check api accessed.")
    return { "status": "success", "message": "API service is running!"}