import requests
import sys
import time
import os
import json
import subprocess

def main():
    print('locate', flush=True)

    audio = sys.stdin.read().strip()

    print(audio[1:20], flush=True)

    url = 'api:5000/api'

    body = {}
    body['audio'] = audio

    resp_preprossessing = requests.post(f'http://{url}/preporessing', json=body)
    preprossessed = resp_preprossessing.json()

    print(preprossessed, flush=True)

    time.sleep(500)

    # response = requests.post(f'http://{url}/detection/getLocation', json=preprossessed)
    # location = response.json()
    # location_json = json.dumps(location)
    location = json.dumps({'hi':1})

    # analyze the location data -> make sure it is resonalble
    resonable = True

    if resonable:
        # drone deployment operations
        command = ["python", "deploy.py", f'{location}']
        process = subprocess.Popen(command, stdin=subprocess.PIPE)



if __name__ == '__main__':
    main()