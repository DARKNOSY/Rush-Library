#upload file using path and transfer.sh

import os
from datetime import datetime
import requests

def upload_file(file_path):
    if '"' in file_path:
        file_path = file_path.replace('"', '')
    try:
        f = open(file_path, "rb")
    except FileNotFoundError:
        print("File was not found!")
        print("Please specify a different path and try again")
        return

        file = {'{}'.format(file_path): f}
        response = requests.post('https://transfer.sh/', files=file)
        download_link = response.content.decode('utf-8')
        deletion_token = response.headers.get("X-Url-Delete")
        deletion_token = deletion_token.replace(download_link.rstrip() + '/', '')

        print("Uploaded file successfully")
        print("Link:")
        print(download_link)
        print("Deletion token:")
        print(deletion_token)

file_path = input("Enter the file path: ")
download_file(file_path)
