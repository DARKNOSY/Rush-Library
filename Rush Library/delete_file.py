# by me

import os

def delete_file(file_path):
    if not file_path:
        return "Please provide a valid file path."

    abs_path = os.path.abspath(file_path)

    if not os.path.exists(abs_path):
        return "The specified file does not exist."

    if not os.path.isfile(abs_path):
        return "The specified path is not a file."

    try:
        # Delete the file
        os.remove(abs_path)
        return f"File '{file_path}' has been successfully deleted."
    except Exception as e:
        return f"An error occurred while deleting the file: {str(e)}"

file_path = input("Enter the file path to delete: ")
result = delete_file(file_path)
print(result)
