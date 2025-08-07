import json
import logging
import os

def load_config():
    default_config = {
        "interval": 300,
        "proxies": []
    }
    config_file = "data/config.json"

    if not os.path.exists(config_file):
        try:
            with open(config_file, 'w', encoding='utf-8') as file:
                json.dump(default_config, file, indent=2, ensure_ascii=False)
            logging.info(f"Created default config file: {config_file}")
        except Exception as e:
            logging.error(f"Failed to create config.json: {e}")
        return default_config

    try:
        with open(config_file, 'r', encoding='utf-8') as file:
            return json.load(file)
    except Exception as e:
        logging.error(f"Failed to load config.json: {e}")
        return default_config
