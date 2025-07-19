import os
import requests


def classify_text(text, labels):
    """
    Classifies a list of text inputs using the Jina API.
    """
    # Ensure the JINA_API_KEY is set in the environment
    api_key = os.getenv('JINA_API_KEY')
    if not api_key:
        raise EnvironmentError("JINA_API_KEY environment variable is not set.")

    url = 'https://api.jina.ai/v1/classify'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }

    data = {
        "model": "jina-embeddings-v3",
        "input": [text],
        "labels": labels
    }

    response = requests.post(url, headers=headers, json=data)

    return response.json()
