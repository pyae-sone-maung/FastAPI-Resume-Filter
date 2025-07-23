import os
from typing import Optional
from config import config_by_name
from werkzeug.utils import secure_filename

env_name = os.environ.get('APP_ENV', 'development')
config = config_by_name.get(env_name, config_by_name["default"])()

def get_file_extension(filename: str) -> Optional[str]:
    if not filename:
        return None
    
    secured_filename = secure_filename(filename)
    if '.' not in secured_filename:
        return None
    
    _, extension = os.path.splitext(secured_filename)
    return extension[1:].lower() if extension else None

def allowed_file(filename: str) -> bool:
    extension = get_file_extension(filename)
    if extension is None:
        return False
    return extension in config.ALLOWED_EXTENSIONS