import requests
import os
url = "http://localhost:8000/api/getLocation"
#file_path = os.path.abspath("Testing.wav")
file_path = "Testing.wav"

files = {"file": open(file_path, "rb")}
response = requests.post(url, files=files)

if response.status_code == 200:
    print(response.json())
else:
    print("Request failed with status code:", response.status_code)
