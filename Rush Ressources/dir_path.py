# by me

import os

def list_directory(path):
    # Get the absolute path of the specified directory
    abs_path = os.path.abspath(path)

    # Check if the specified directory exists
    if not os.path.exists(abs_path):
        return "Directory does not exist."

    # Check if the specified path is a file
    if os.path.isfile(abs_path):
        return "The specified path is a file, not a directory."

    # Get all items in the specified directory
    items = os.listdir(abs_path)

    # Format the items into a string
    items_string = "\n".join(items)

    return f"Items in {abs_path}:\n{items_string}"

path = input("Enter a directory path: ")
directory_items = list_directory(path)
print(directory_items)
