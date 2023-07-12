import requests
import sys
import time
import os
import json
import subprocess
import requests

def main():
    # db_index= sys.argv[1]

    audio = sys.stdin.read().strip()

    url = 'api:5000/api'

    body = {}
    body['audio'] = audio

    # noice code  
    # resp_preprossessing = requests.post(f'http://{url}/preporessing', json=body)
    # preprossessed = resp_preprossessing.json()

    response = requests.post(f'http://{url}/getLocation', json=body)
    location = response.json()
    location = json.dumps(location)

    print(f'{location} (acustic model)', flush=True)

    # analyze the location data -> make sure it is resonalble
    resonable = True

    if resonable:
        # drone deployment operations
        command = ["python", "deploy.py", f'{location}']
        process = subprocess.Popen(command, stdin=subprocess.PIPE)



if __name__ == '__main__':
    main()