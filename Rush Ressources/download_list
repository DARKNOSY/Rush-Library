# by me

import os

def get_downloads():
    download_folder = os.path.expanduser("~\\Downloads")
    files = os.listdir(download_folder)
    if not files:
        print("No files found")
        return
    file_list = "\n".join(files)
    with open("downloads.txt", "w", encoding="utf-8") as file:
        file.write(file_list)
    print("Download file list generated.")

get_downloads()
