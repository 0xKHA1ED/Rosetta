import logging
import random
import json
import time
from urllib.parse import urlparse
from utils import app_setup
from utils.file_utils import read_chat_log, save_organized_urls
from utils.url_utils import extract_urls
from utils.scraping_utils import log_skipped_url
from src.scraper import scraping_url
from utils.file_utils import load_json_data
from src.classify import classify_text
from utils.classification_utils import get_most_likely_categories
# from utils.token_count import count_tokens_with_tiktoken
from utils.summarizer import summarize_text


def run_application(config):
    """
    The main logic of the application.
    """
    logging.info("Application is running.")
    chat_log = read_chat_log(config['chat_log_file_path'])
    if not chat_log:
        return
    logging.info("Chat log read successfully.")

    organized_urls = extract_urls(chat_log)
    if not organized_urls:
        return
    logging.info("URLs extracted successfully.")

    output_filepath = save_organized_urls(organized_urls, config['output_file_path'])
    if not output_filepath:
        return
    logging.info(f"Organized URLs saved to {output_filepath}.")

    all_urls = [url for urls_list in organized_urls.values() for url in urls_list]
    random.shuffle(all_urls)
    logging.info("URL list has been randomized.")

    # Scraping URLs
    success_count = 0
    for url in all_urls:
        domain = urlparse(url).netloc
        if any(skip_keyword in domain for skip_keyword in config['skip_domains']):
            log_skipped_url(url, config)
            logging.info(f"Skipping domain: {domain}")
            continue

        if scraping_url(url, config):
            logging.info(f"Successfully scraped: {url}")
            success_count += 1
        else:
            logging.error(f"Failed to scrape: {url}")

        if success_count >= config['max_scraped_items']:
            logging.info(f"Reached maximum scraped items limit: {config['max_scraped_items']}. Stopping.")
            break

    # Classifying scraped content
    if success_count > 0:
        logging.info(f"Classifying {success_count} scraped items.")

        # Load classification labels from config
        labels = config.get('classification_labels', [])

        data = load_json_data(config['scraped_data_file_path'])
        for item in data:
            if item['summarized'] is True:
                continue

            # Check if there is content to classify
            content = item.get('content', '')
            if content:
                summarized_content = summarize_text(content)
                if summarized_content:
                    item['content'] = summarized_content
                    item['summrized'] = True
                    logging.info(f"Content for {item['url']} summarized due to token limit.")
                else:
                    logging.warning(f"Failed to summarize content for {item['url']}. Skipping classification.")
                    continue

                classification_result = classify_text(item['content'], labels)
                most_likely_categories = get_most_likely_categories(classification_result, n=3)
                item['classification'] = most_likely_categories
                print(f"Classified '{item['title'][:40]}...' as: {most_likely_categories}")
            time.sleep(1)

        # Save the classified data back to the file
        with open(config['scraped_data_file_path'], 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        logging.info("Classification complete and results saved.")


if __name__ == "__main__":
    # 1. Perform all initial setup by calling one function.
    app_setup.setup_logging()

    # 2. Load configuration.
    try:
        app_config = app_setup.load_config()
    except FileNotFoundError:
        exit()

    # 3. Run the main application.
    run_application(app_config)
