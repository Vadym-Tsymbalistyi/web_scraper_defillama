import json
import logging
import os

def save_to_json(data, filename="data/data.json"):
    try:
        if not os.path.exists(filename):
            with open(filename, "w", encoding="utf-8") as f:
                json.dump([], f, indent=2, ensure_ascii=False)
            logging.info(f"Created empty data file: {filename}")

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        logging.info("Scraped data successfully saved to JSON file")
    except Exception as e:
        logging.error(f"Error occurred while saving data to JSON file: {e}")
