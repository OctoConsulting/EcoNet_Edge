import requests
import sys
import time
import os
import json
import subprocess
import requests

def main():
    # db_index= sys.argv[1]
    time= sys.argv[2]

    audio = sys.stdin.read().strip()

    url = 'api:5000/api'

    body = {}
    body['audio'] = audio

    # noice code  
    # resp_preprossessing = requests.post(f'http://{url}/preporessing', json=body)
    # preprossessed = resp_preprossessing.json()

    response = requests.post(f'http://{url}/getLocation', json=body)
    location = response.json()

    # location into db :)
    # shot_data= {'microphone_angle': location['Angle'],
    #             'shooter_angle': location['Azimuth'],
    #             'distance': location['Distance'],
    #             'id': db_index}
    # json_headers= {'Content-Type': 'application/json'}
    # db_index= requests.post(f'http://db_courier:5000/put_shot_acoustic_model',
    #                        data= shot_data,
    #                        headers= json_headers)

    location = json.dumps(location)

    print(f'[{time}] {location} (acoustic model)', flush=True)
    # analyze the location data -> make sure it is resonalble
    resonable = True

    if resonable:
        # drone deployment operations
        command = ["python", "deploy.py", f'{location}']
        process = subprocess.Popen(command, stdin=subprocess.PIPE)

        # start the feed
        requests.get('http://reverse_proxy:80/video/start_drone1')



if __name__ == '__main__':
    main()