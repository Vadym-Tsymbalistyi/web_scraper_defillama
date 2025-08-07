import logging
import os

def setup_logging():
    log_file = "logs/scraper.log"
    if not os.path.exists(log_file):
        open(log_file, 'a').close()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    logging.info("Logging setup completed")
