import os
import logging
import json


def read_chat_log(chat_log_path):
    """
    Reads the chat log from the specified path and returns its content.

    :param chat_log_path: Path to the chat log file.
    :return: Content of the chat log file as a string.
    """
    if not os.path.exists(chat_log_path):
        logging.error(f"Chat log file {chat_log_path} does not exist.")
        return None
    else:
        try:
            with open(chat_log_path, "r", encoding="utf-8") as f:
                return f.read()
        except Exception as e:
            logging.error(f"Error reading chat log: {e}")
            return None


def save_organized_urls(organized_data, output_filepath="extracted_urls.txt"):
    """
    Saves the organized URLs to a text file, grouped by root domain.
    """
    if not organized_data:
        print("No URLs to save. The input file might be empty or contained unparsable URLs.")
        return
    try:
        with open(output_filepath, 'w') as f:
            # Sort domains alphabetically for consistent output
            sorted_domains = sorted(organized_data.keys())
            for domain in sorted_domains:
                urls = organized_data[domain]
                for url in urls:
                    f.write(f"{url}\n")
    except Exception as e:
        logging.error(f"Error saving organized URLs: {e}")
        return None

    return output_filepath


def read_organized_urls(file_path='organized_urls.txt'):
    """
    Reads organized URLs from a file and returns them as a list.

    :param file_path: Path to the file containing organized URLs.
    :return: List of URLs read from the file.
    """
    if not os.path.exists(file_path):
        print(f"\n{file_path} does not exist.")
        return []
    with open('organized_urls.txt', 'r', encoding='utf-8') as file:
        urls = file.readlines()
    return urls


def load_json_data(input_filepath):
    """
    Loads JSON data from the specified input file.

    :param input_filepath: Path to the input JSON file.
    :return: Parsed JSON data as a list or dictionary.
    """
    try:
        with open(input_filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        print(f"Error: Input file '{input_filepath}' not found.")
        return
