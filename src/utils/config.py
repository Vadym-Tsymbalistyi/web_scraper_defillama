from pathlib import Path
from typing import List

import yaml
from pydantic import BaseModel


class AppConfig(BaseModel):
    target_url: str
    pulling_interval_in_sec: int
    proxies: List[str]
    result_output_base_dir: str
    result_output_base_file_name: str


class Config(BaseModel):
    app: AppConfig


def load_app_config(config_path: Path) -> AppConfig:
    """Loads YAML configuration from a file into a Pydantic Config object."""
    try:
        app_config_yaml = read_yaml_config(config_path)
        return Config(**app_config_yaml).app
    except FileNotFoundError:
        raise FileNotFoundError(f"Configuration file not found at: {config_path}")
    except yaml.YAMLError as e:
        raise ValueError(f"Error parsing YAML file: {e}")
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {e}")


def read_yaml_config(config_path):
    with open(config_path, 'r') as f:
        return yaml.safe_load(f.read())
