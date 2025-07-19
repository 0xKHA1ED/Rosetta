from utils.app_setup import load_config


config = load_config()


def log_failed_url(url, output_file=config['failed_urls_file_path']):
    """Appends a failed URL to the designated log file."""
    with open(output_file, 'a', encoding='utf-8') as f:
        f.write(url + '\n')


def log_skipped_url(url, output_file=config['skipped_urls_file_path']):
    """Appends a skipped URL to the designated log file."""
    with open(output_file, 'a', encoding='utf-8') as f:
        f.write(url + '\n')
