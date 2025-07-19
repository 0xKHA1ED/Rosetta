from google import genai
import logging


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
        response = client.generate_text(
            model=model,
            prompt=f"Summarize the following text to a maximum of 500 words:\n\n{text}"
        )
        return response.text.strip()
    except Exception as e:
        logging.error(f"Error summarizing text: {e}")
        return False
