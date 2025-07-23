import os
import logging

def setup_logging(debug_mode: bool):
    logger = logging.getLogger("main_app_logger")
    if logger.handlers:
        for handler in logger.handlers:
            logger.removeHandler(handler)
            
    log_level = logging.INFO if debug_mode else logging.WARNING
    logger.setLevel(log_level)
    
    log_dir = 'logs'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
        
    log_file_path = os.path.join(log_dir, 'app.log')
    
    console_format = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    file_format = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(module)s - %(funcName)s - %(lineno)d - %(message)s'
    )
    
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(console_format)
    logger.addHandler(console_handler)
    
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setLevel(log_level)
    file_handler.setFormatter(file_format)
    logger.addHandler(file_handler)
    
    logger.propagate = False
    
    return logger