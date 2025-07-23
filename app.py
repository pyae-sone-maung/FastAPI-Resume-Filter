import os
from fastapi import FastAPI
from src.app.routes import router as api_router
from config import config_by_name
from src.app.core.logging_handlers.logging_config import setup_logging
from src.app.core.exception_handlers.exception_handler import register_exception_handlers

env_name = os.environ.get('APP_ENV', 'development')
config = config_by_name.get(env_name, config_by_name["default"])()
app_logger = setup_logging(config.DEBUG)

app = FastAPI(
    title = config.APP_TITLE,
    version= config.APP_VERSION,
    debug=config.DEBUG
)

register_exception_handlers(app)
app.include_router(api_router, prefix="/api/v1")
