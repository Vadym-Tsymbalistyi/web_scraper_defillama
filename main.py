import time
import logging
from utils.logger_setup import setup_logging
from config.config import load_config
from utils.driver import create_driver
from scraper.scraper import scrape_page
from utils.storage import save_to_json

def run():
    setup_logging()
    config = load_config()
    interval = config.get("interval", 300)
    proxies = config.get("proxies", [])

    driver = None
    try:
        while True:
            logging.info("Web scraping started...")
            if not driver:
                driver = create_driver(proxies)
                if not driver:
                    logging.error("Failed to initialize WebDriver. Retrying in 60 seconds.")
                    time.sleep(60)
                    continue

            data = scrape_page(driver)
            save_to_json(data)

            logging.info(f"Web scraping process completed. Sleeping for {interval} seconds.")
            time.sleep(interval)
    except KeyboardInterrupt:
        logging.info("Scraper manually stopped. Cleaning up...")
    finally:
        if driver:
            driver.quit()
        logging.info("Resources cleaned up successfully. Exiting.")

if __name__ == '__main__':
    run()
