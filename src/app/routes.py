from fastapi import APIRouter
import logging
from src.app.controllers.resume_controller import router as resume_router

logger = logging.getLogger("main_app_logger")
router = APIRouter()

router.include_router(resume_router)

@router.get("/health")
def health_check():
    logger.info(f"Health check api accessed.")
    return { "status": "success", "message": "API service is running!"}