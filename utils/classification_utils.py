def get_most_likely_categories(data, n=3):
    """
    Extracts the most likely categories from the Jina API response.
    :param data: The JSON response from the Jina API.
    :param n: The number of top categories to return.
    :return: A list of the top n categories.
    """

    predictions = data['data'][0]['predictions']
    if not predictions:
        return []
    # Sort predictions by score in descending order
    sorted_predictions = sorted(predictions, key=lambda x: x['score'], reverse=True)
    # Return the top n categories
    return [pred['label'] for pred in sorted_predictions[:n]]
