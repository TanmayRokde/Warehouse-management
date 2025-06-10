import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[
        logging.FileHandler("mapping.log"),
        logging.StreamHandler()
    ],
)

def log_info(message):
    logging.info(message)

def log_warning(message):
    logging.warning(message)
