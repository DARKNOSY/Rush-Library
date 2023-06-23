# by me

import os

def list_directory():
    # Get the current directory
    current_dir = os.getcwd()

    # Get all items in the directory
    items = os.listdir(current_dir)

    # Format the items into a string
    items_string = "\n".join(items)

    return items_string

# Usage example
directory_items = list_directory()
print(f"Items in current directory:\n{directory_items}")
