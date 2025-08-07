import json
import logging
import os


class OutputWriter:
    def __init__(self, base_path):
        self.logger = logging.getLogger("OutputWriter")
        self.base_path = base_path

    def save_to_json(self, data, path="data/data.json"):
        try:
            if not os.path.exists(path):
                with open(path, "w", encoding="utf-8") as f:
                    json.dump([], f, indent=2, ensure_ascii=False)
                self.logger.info(f"Created empty data file: {path}")

            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            self.logger.info("Scraped data successfully saved to JSON file")
        except Exception as e:
            self.logger.error(f"Error occurred while saving data to JSON file: {e}")
            raise
