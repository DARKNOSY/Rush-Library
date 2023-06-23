# by me

import os

def get_path_file(filename):
    if not filename:
        return "Please provide a valid filename."

    abs_path = os.path.abspath(filename)

    if not os.path.exists(abs_path):
        return "The specified file does not exist."

    return abs_path

filename = input("Enter the filename to get the path: ")
result = get_path_file(filename)
print(result)
