import os

class Config:
    DEBUG = False
    APP_TITLE = "Resume Filter API Service"
    APP_VERSION = "0.0.1"
    
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