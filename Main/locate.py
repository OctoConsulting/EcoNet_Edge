import requests
import sys
import time
import os
import json
import subprocess
import requests
from datetime import datetime, timedelta
from pytz import timezone

def main():
    db_index= sys.argv[1]
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

    # Populate database with relative coords
    # we must format it the way the db understands
    coords= {'microphone_angle': location['Angle'],
             'shooter_angle': location['Azimuth'],
             'distance': location['Distance'],
             'gun_type': location['Weapon']}
    print('adding relative coords:', coords)
    response = requests.put(f'http://db_courier:5000/update_shot/{str(db_index)}', json=coords)
    print('adding relative coords resulted in', response, 'status')
    location = json.dumps(location)

    current_time= datetime.now(timezone('America/New_York')).strftime("%H-%M-%S")
    print(f'shot time: [{time}] eval time: [{current_time}] {location} (acoustic model)', flush=True)

    # analyze the location data -> make sure it is resonalble
    resonable = True

    if resonable:
        # drone deployment operations
        command = ["python", "deploy.py", f'{location}']
        process = subprocess.Popen(command, stdin=subprocess.PIPE)

if __name__ == '__main__':
    main()