import logging
import logging.config
import time
from pathlib import Path

from src.scraper.scraper import Scraper
from src.utils.config import load_app_config
from src.utils.config import read_yaml_config
from src.utils.output_writer import OutputWriter


def run():
    logging.debug("Setup logging")
    logging.config.dictConfig(read_yaml_config('config/logging.yaml'))
    logging.debug("Logging setup completed")

    logging.debug("Load App config")
    app_config = load_app_config(Path("config/app.yaml"))

    logging.info(f"Run the Scraper App with the app config: {app_config}")
    scraper = Scraper(app_config.target_url, app_config.proxies)
    output_writer = OutputWriter(app_config.result_output_base_dir, app_config.result_output_base_file_name)

    try:
        while True:
            logging.info("Web scraping started...")

            scraping_result = scraper.scrape_page()
            output_writer.save_to_json(scraping_result)

            logging.info(f"Web scraping process completed. Sleeping for {app_config.pulling_interval_in_sec} seconds.")
            time.sleep(app_config.pulling_interval_in_sec)
    except KeyboardInterrupt:
        logging.info("Scraper was stopped manually. Cleaning up...")
    finally:
        scraper.stop()
        logging.info("Resources cleaned up successfully. Exiting.")


if __name__ == '__main__':
    run()
