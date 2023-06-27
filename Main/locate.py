import requests
import sys
import time
import os
import json

def main():
    print('locate')

    audio = sys.stdin.read().strip()

    url = 'api:5000/api'

    body = {}
    body['audio'] = audio

    resp_preprossessing = requests.post(f'http://{url}/preporessing', json=body)
    preprossessed = resp_preprossessing.json()

    response = requests.post(f'http://{url}/detection/getLocation', json=preprossessed)
    location = response.json()
    location_json = json.dumps(location)

    # analyze the location data -> make sure it is resonalble
    resonable = True

    if resonable:
        # drone deployment operations
        if os.fork() != 0:
            program_path = 'deploy.py'
            os.execlp('python3', program_path, location_json)


if __name__ == '__main__':
    main()