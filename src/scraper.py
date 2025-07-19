import requests
import json
import logging
import os
from utils.scraping_utils import log_failed_url


def save_data_as_json_list(item_dict, config):
    """Reads the JSON file, appends a new item, and writes it back."""
    data = []
    try:
        with open(config['scraped_data_file_path'], 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            # Ensure it's a list
            if not isinstance(data, list):
                logging.warning(f"{config['scraped_data_file_path']} is not a list. Starting fresh.")
                data = []
    except (FileNotFoundError, json.JSONDecodeError):
        # File doesn't exist or is empty/corrupt, start with an empty list
        data = []

    data.append(item_dict)

    with open(config['scraped_data_file_path'], 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


def scraping_url(url, config):
    api_key = os.getenv('JINA_API_KEY')
    if not api_key:
        logging.critical("Error: JINA_API_KEY environment variable is not set.")
        return

    headers = {
        'Authorization': f'Bearer {api_key}',
        'Accept': 'application/json'
    }

    jina_url = f"https://r.jina.ai/{url}"

    item_dict = {}

    try:
        # Make the GET request with a timeout to prevent indefinite hanging
        response = requests.get(jina_url, headers=headers, timeout=30)
        # Raise an exception for bad status codes (4xx or 5xx)
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()
        # Safely extract the title and content from the response data
        title = data.get('data', {}).get('title')
        content = data.get('data', {}).get('content')

        # If content is not found in the JSON, log a warning and fall back to raw text
        if not content:
            logging.warning(f"No content found in JSON response for {url}. Falling back to raw text.")
            content = response.text

        # Prepare the dictionary to be saved as a JSON line
        item_dict = {
            'url': url,
            'title': title,
            'content': content,
            'classification': 'Unclassified'
        }

    except requests.exceptions.RequestException as err:
        logging.error(f"Request failed for {url}: {err}")
        log_failed_url(url, config)

    # Handle cases where the response is not valid JSON
    except json.JSONDecodeError:
        logging.error(f"Failed to decode JSON for {url}. Saving raw text content.")
        log_failed_url(url, config)
        # Create a fallback dictionary with the raw text
        item_dict = {
            'url': url,
            'title': "No title available",
            'content': response.text,
            'classification': "Unclassified"
        }

    if item_dict:
        save_data_as_json_list(item_dict, config)
        # logging.info(f"Successfully saved data for: {url}")
        return True
    return False
