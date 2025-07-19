import logging
import json
import os


def setup_logging():
    """
    Configures logging for the entire application.
    This should be the first function called.
    """
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )


def load_config(config_path='config.json'):
    """
    Loads the JSON configuration file.
    """
    if not os.path.exists(config_path):
        logging.error(f"Configuration file not found at {config_path}")
        raise FileNotFoundError(f"Configuration file not found at {config_path}")

    with open(config_path, 'r') as f:
        config = json.load(f)
    logging.info("Configuration loaded successfully.")
    return config
