import tiktoken


def count_tokens_with_tiktoken(text, model_name="gpt-3.5-turbo"):
    """
    Counts tokens in a string using OpenAI's tiktoken library.

    Args:
        text (str): The input text.
        model_name (str): The name of the OpenAI model to use for encoding.

    Returns:
        int: The number of tokens in the text.
    """
    try:
        encoding = tiktoken.encoding_for_model(model_name)
    except KeyError:
        # Fallback to a common encoding if the model name isn't directly found
        encoding = tiktoken.get_encoding("cl100k_base")
        print(f"Warning: Model '{model_name}' not found. Using 'cl100k_base' encoding.")

    tokens = encoding.encode(text)
    return len(tokens)
