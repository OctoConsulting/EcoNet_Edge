import requests

import os

url = "http://localhost:8000/api/detection/detectShot"

#file_path = os.path.abspath("Testing.wav")

# file_path = "Testing.wav"


output_path = "UPDATEWORK.txt"

# files = {"file": open(file_path, "rb")}

response = requests.post(url)


if response.status_code == 200:

    with open(output_path, "wb") as f:

        f.write(response.content)

    print("File saved successfully")

else:

    print("Request failed with status code:", response.status_code)