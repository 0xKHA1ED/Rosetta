import json

def print_urls_non_recursive(data):
    counter = 0
    word_count = 0
    urls = []
    # Initialize a stack with the top-level data.
    # Since we know it's a list of objects, we add its elements.
    if not isinstance(data, list):
        print("Error: Expected a list of objects at the top level.")
        return

    stack = list(data) # Start with all top-level objects in the stack

    while stack:
        current_item = stack.pop() # Get an item from the stack (DFS-like)

        if isinstance(current_item, dict):
            # Check for 'url' in the current dictionary
            if "url" in current_item and isinstance(current_item["url"], str):
                # print(current_item["url"])
                if current_item["url"] not in urls:
                    urls.append(current_item["url"])
                print(len(current_item["content"].split()))
                word_count += len(current_item["content"].split())
                counter += 1

            # Add all values (which could be nested objects or lists) to the stack
            for value in current_item.values():
                if isinstance(value, (dict, list)): # Only add complex types
                    stack.append(value)
        elif isinstance(current_item, list):
            # If it's a list, add all its elements to the stack
            for item in current_item:
                if isinstance(item, (dict, list)): # Only add complex types
                    stack.append(item)
    print(f"Total URLs found: {counter}")
    print(f"Total words counted: {word_count}")
    print("Unique URLs Count: ", len(urls))

file_path = 'scraped_data.json'

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
        print_urls_non_recursive(json_data)
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
except json.JSONDecodeError as e:
    print(f"Error decoding JSON from '{file_path}': {e}")