import logging
from google import genai


def summarize_text(text, model="gemini-2.5-flash"):
    """
    Summarizes the given text using Google's GenAI model.

    Args:
        text (str): The text to summarize.
        model (str): The GenAI model to use for summarization.

    Returns:
        str: The summarized text.
    """
    try:
        client = genai.Client()
        with open('utils/prompt.txt', 'r') as f:
            prompt = f.read()
        response = client.models.generate_content(
            model=model,
            contents=f"{prompt}\n\n{text}",
        )
        return response.text.strip()
    except Exception as e:
        logging.error(f"Error summarizing text: {e}")
        return False
