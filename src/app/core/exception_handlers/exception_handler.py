import logging
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from src.app.core.exception_handlers.exception_config import APIError

logger = logging.getLogger("main_app_logger")

def register_exception_handlers(app: FastAPI):
    @app.exception_handler(APIError)
    async def api_error_handler(request: Request, exc: APIError):
        logger.error(f"Error : {exc.message} - Status: {exc.status_code} - URL: {request.url}")
        return JSONResponse(
            status_code=exc.status_code,
            content={"message": exc.message}
        )
        
    @app.exception_handler(StarletteHTTPException)
    async def http_exception_handler(request: Request, exc: StarletteHTTPException):
        if exc.status_code == status.HTTP_400_BAD_REQUEST:
            logger.warning(f"400 Bad Request: {request.url} - Message: {exc.detail}")
            return JSONResponse(
                status_code = status.HTTP_400_BAD_REQUEST,
                content = {"message": "Bad Request"}
            )
        elif exc.status_code == status.HTTP_401_UNAUTHORIZED:
            logger.warning(f"401 Unauthorized: {request.url} - Message: {exc.detail}")
            return JSONResponse(
                status_code = status.HTTP_401_UNAUTHORIZED,
                content = {"message": "Unauthorized"}
            )
        elif exc.status_code == status.HTTP_404_NOT_FOUND:
            logger.warning(f"404 Not found: {request.url} - Message: {exc.detail}")
            return JSONResponse(
                status_code = status.HTTP_404_NOT_FOUND,
                content = {"message": "Not found"}
            )
        elif exc.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR:
            logger.error(f"500 Internal server error: {request.url} - Message:{exc.detail}")
            return JSONResponse(
                status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
                content = {"message": "Internal server error"}
            )
        else:
            logger.error(f"HTTP Exception { exc.status_code}: {request.url} - Message: {exc.detail}")
            return JSONResponse(
                status_code = exc.status_code,
                content = {"message": "An HTTP error occured."}
            )
            
    @app.exception_handler(Exception)
    async def general_exception_handler(request: Request, exc: Exception):
        logger.exception(f"Internal Server Error: {request.url} - Exception: {exc}")
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": "An unexpected error occurred. Please try again later."},
        )
