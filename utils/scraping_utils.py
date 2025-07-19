def log_failed_url(url, output_file='failed_urls.txt'):
    """Appends a failed URL to the designated log file."""
    with open(output_file, 'a', encoding='utf-8') as f:
        f.write(url + '\n')


def log_skipped_url(url):
    """Appends a skipped URL to the designated log file."""
    with open('skipped_urls.txt', 'a', encoding='utf-8') as f:
        f.write(url + '\n')
