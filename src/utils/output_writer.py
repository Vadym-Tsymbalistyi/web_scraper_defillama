import json
import logging
import os
from datetime import datetime
from pathlib import Path


class OutputWriter:
    def __init__(self, base_dir, base_file_name):
        self.logger = logging.getLogger("OutputWriter")
        self.base_dir = Path(base_dir)
        self.base_file_name = Path(base_file_name)
        self.__init_base_dir()

    def __init_base_dir(self):
        if not os.path.exists(self.base_dir):
            try:
                self.logger.info(f"The base dir '{self.base_dir}' doesn't exist yet. Creating it...")
                self.base_dir.mkdir(parents=True, exist_ok=True)
                self.logger.info(f"The base dir '{self.base_dir}' is created")
            except OSError as e:
                print(f"Couldn't create the base dir '{self.base_dir}': {e}")

    def save_to_json(self, data):
        # Get the current date and time
        now = datetime.now()

        # Format the timestamp
        # "%Y-%m-%d_%H-%M-%S" for YYYY-MM-DD_HH-MM-SS (e.g., 2025-08-07_20-41-00)
        timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")

        # Construct the full filename with the timestamp suffix
        full_filename = f"{self.base_dir}/{self.base_file_name}_{timestamp}" + ".json"

        # Create and write to the file
        try:
            with open(full_filename, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=2, ensure_ascii=False)
                self.logger.info(f"Scraped data successfully saved to the JSON file: '{full_filename}'")
        except IOError as e:
            self.logger.error(f"Error occurred while saving data to '{full_filename}': {e}")
            raise
