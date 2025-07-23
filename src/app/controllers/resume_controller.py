import os
import json
import logging
from fastapi import APIRouter, status
from src.app.services.resume_service import resume_service
from src.app.dtos.base_response import BaseResponse
from config import config_by_name

logger = logging.getLogger("main_app_logger")
env_name = os.environ.get('APP_ENV', 'development')
config = config_by_name.get(env_name, config_by_name["default"])()

router = APIRouter(prefix="/resume", tags=["Resume"])

@router.get("/resume-data")
async def get_resume_data():
    try:
        upload_file = os.path.join(config.UPLOAD_FOLDER, "AKK.pdf")

        if not os.path.exists(upload_file):
            return BaseResponse.fail_response(
                message="File not found."
            ).to_json_response(status_code=status.HTTP_404_NOT_FOUND)
        else:
            resume_data_raw = await resume_service.get_porcessed_resume_data(upload_file)
            if resume_data_raw is None:
                resume_data = {}
            else:
                resume_data = json.loads(resume_data_raw)
            
            return BaseResponse.success_response(
                message="Resume data retrieved successfully.",
                data=resume_data
            ).to_json_response(status_code=status.HTTP_200_OK)
    except Exception as ex:
        logger.error(f"An unexpected error occurred in get_resume_data: {ex}", exc_info=True)
        BaseResponse.raise_exception(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message="An unexpected error occured.",
            error=str(ex)
        )