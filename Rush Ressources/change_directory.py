# adapted by me

import os

def change_directory(directory):
    try:
        os.chdir(directory)
        print(f"Changed directory to: {os.getcwd()}")
    except Exception as e:
        print("An error occurred while changing the directory:")
        print(str(e))

directory = input("Enter the directory path: ")
change_directory(directory)
