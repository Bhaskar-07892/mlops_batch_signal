import logging
import os
from datetime import datetime

def get_logger(log_dir = "logs" , level = logging.INFO) -> logging.Logger : 
    os.makedirs(log_dir ,exist_ok=True)

    log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

    log_file_path = os.path.join(log_dir , log_file)

    logger = logging.getLogger("mlops_batch_signal")
    logger.setLevel(level)
    logger.propagate = False

    if not logger.handlers:

        file_handler = logging.FileHandler(log_file_path)
        formatter = logging.Formatter(
            "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
        )
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger