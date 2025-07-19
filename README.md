# Rosetta: Web Content Scraper

Rosetta is a Python-based web scraper that extracts URLs from a chat log, fetches their content using the Jina AI reader API, and saves the structured data to a JSON file. It's designed to efficiently process and archive web content from conversations.

## Features

- **URL Extraction**: Automatically extracts and organizes URLs from a specified chat log file.
- **Content Scraping**: Uses the Jina AI reader API (`https://r.jina.ai/`) to scrape the title and main content of web pages.
- **Data Storage**: Saves the scraped data (URL, title, content) in a clean, structured JSON format.
- **Configurable**: Easily configure file paths, domains to skip, and scraping limits through a `config.json` file.
- **Error Handling**: Logs skipped domains, failed requests, and other errors for easier debugging.
- **Environment Variable Support**: Securely uses a `JINA_API_KEY` from environment variables for API authentication.

## Requirements

- Python 3.x
- `requests` library

You can install the required Python package using pip:
```bash
pip install -r requirements.txt
```

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/0xKHA1ED/Rosetta.git
    cd Rosetta
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up the environment variable:**
    You need a Jina AI API key to use the scraper. Export it as an environment variable:
    ```bash
    export JINA_API_KEY='your_jina_api_key'
    ```
    To make this permanent, add the line to your shell's configuration file (e.g., `.bashrc`, `.zshrc`).

4.  **Configure the application:**
    Create a `config.json` file in the root directory. You can use the following template:
    ```json
    {
      "chat_log_file_path": "data/chat.log",
      "output_file_path": "output/organized_urls.txt",
      "scraped_data_file_path": "output/scraped_data.json",
      "skip_domains": [
        "youtube.com",
        "youtu.be"
      ],
      "max_scraped_items": 100
    }
    ```

## Usage

1.  Place your chat log file in the location specified in `config.json` (e.g., `data/chat.log`).
2.  Run the main script from the root directory:
    ```bash
    python main.py
    ```
3.  The application will:
    - Read the chat log and extract URLs.
    - Save the organized URLs to the path specified in `output_file_path`.
    - Scrape each URL and save the content to `scraped_data_file_path`.

## Configuration

The `config.json` file allows you to customize the application's behavior:

-   `chat_log_file_path`: Path to the input chat log file.
-   `output_file_path`: Path to save the organized list of extracted URLs.
-   `scraped_data_file_path`: Path to save the final scraped data in JSON format.
-   `skip_domains`: A list of domains to ignore during scraping.
-   `max_scraped_items`: The maximum number of URLs to scrape before stopping.
