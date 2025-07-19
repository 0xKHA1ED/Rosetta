import re
from collections import defaultdict
import tldextract
import logging


def get_unique_urls(urls):
    """
    Returns a list of unique URLs from the provided list.
    """
    return list(set(urls))


def get_clean_urls(urls):
    """
    Cleans the list of URLs by removing any leading/trailing whitespace
    and ensuring they are valid URLs.
    """
    return [url.strip() for url in urls if url.strip()]


def organize_urls_by_domain(urls):
    """
    Reads URLs from a file and organizes them into a dictionary
    where keys are root domains (e.g., 'google.com', 'openai.com')
    and values are lists of URLs belonging to that root domain.
    """
    domain_to_urls = defaultdict(list)

    for url in urls:
        try:
            # Use tldextract to get the root domain components
            extracted = tldextract.extract(url)

            # tldextract returns domain and suffix (e.g., 'google', 'com')
            # Combine them to get the root domain (e.g., 'google.com')
            if extracted.domain and extracted.suffix:
                root_domain = f"{extracted.domain}.{extracted.suffix}"
                domain_to_urls[root_domain].append(url)
            else:
                logging.warning(f"Could not extract root domain from URL: {url}")

        except Exception as e:
            # Catch potential errors from urlparse if the URL is severely malformed
            logging.error(f"Error processing URL '{url}': {e}")

    return domain_to_urls


def extract_urls(text):
    """
    Extracts all URLs from a given text.
    """
    url_pattern = re.compile(
        r'(?:(?:https?|ftp)://|www\.)'
        r'(?:[a-zA-Z0-9.\-]+(?:\.[a-zA-Z]{2,})?)'
        r'(?:[/\\?#][^\s"\'<>{}|\\^`[\]]*)?'
    )
    urls = url_pattern.findall(text)
    unique_urls = get_unique_urls(urls)
    if not unique_urls:
        logging.info("No URLs extracted from the chat log.")
        return []

    # Clean and organize the URLs
    clean_urls = get_clean_urls(unique_urls)
    organized_urls = organize_urls_by_domain(clean_urls)
    return organized_urls
