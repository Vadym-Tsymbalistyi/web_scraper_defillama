import time
import logging

from src.scraper.scraper import Scraper
from utils.logger_setup import setup_logging
from config.config import load_config
from utils.output_writer import OutputWriter

def run():
    setup_logging()
    config = load_config() #TODO: model for config
    interval = config.get("interval", 300)
    proxies = config.get("proxies", [])

    scraper = Scraper(proxies)
    output_writer = OutputWriter("data")

    try:
        while True:
            logging.info("Web scraping started...")

            scraping_result = scraper.scrape_page()
            output_writer.save_to_json(scraping_result)

            logging.info(f"Web scraping process completed. Sleeping for {interval} seconds.")
            time.sleep(interval)
    except KeyboardInterrupt:
        logging.info("Scraper was stopped manually. Cleaning up...")
    finally:
        scraper.stop()
        logging.info("Resources cleaned up successfully. Exiting.")

if __name__ == '__main__':
    run()
