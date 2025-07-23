import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    DEBUG = False
    APP_TITLE = "Resume Filter API Service"
    APP_VERSION = "0.0.1"
    UPLOAD_FOLDER = os.path.join(basedir, 'src', 'assets', 'uploads')
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'pdf', 'docx', 'xlsx'}
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024
    
class DevelopmentConfig(Config):
    DEBUG = True
    RELOAD = True
    HOST = "localhost"
    PORT = 5000
    
class ProductionConfig(Config):
    DEBUG = False
    RELOAD = False
    
config_by_name = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}