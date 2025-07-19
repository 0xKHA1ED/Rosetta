def log_failed_url(url, config):
    """Appends a failed URL to the designated log file."""
    output_file = config.get('failed_urls_file_path', 'failed_urls.txt')
    with open(output_file, 'a', encoding='utf-8') as f:
        f.write(url + '\n')


def log_skipped_url(url, config):
    """Appends a skipped URL to the designated log file."""
    output_file = config.get('skipped_urls_file_path', 'skipped_urls.txt')
    with open(output_file, 'a', encoding='utf-8') as f:
        f.write(url + '\n')
