import simple_websocket
import os
import sys
import requests
import base64
import subprocess
import json


def main():
    PARENT_PID = os.getpid()

    url = 'api:5000/api'

    ws = simple_websocket.Client(f'ws://{url}/detection/audio')

    try:
        while True:
            byte_array = ws.receive()
            base64_bytes = base64.b64encode(byte_array)
            
            a = {}
            a['audio'] = base64_bytes.decode('utf-8')

            response = requests.post(f'http://{url}/detection/detectShot', json=a)

            resp_json = response.json()
            shot = resp_json.get('shot')

            if shot:
                # Define the command and arguments
                command = ["python", "locate.py"]

                # Launch the subprocess and redirect stdout to a pipe
                process = subprocess.Popen(command, stdin=subprocess.PIPE)

                # Send data to the subprocess
                data = json.dumps(a['audio']).encode("utf-8")  # Encode the string as bytes
                process.stdin.write(data)
                process.stdin.close() 
                    

                        
    except (KeyboardInterrupt, EOFError, simple_websocket.ConnectionClosed):
        ws.close()


if __name__ == '__main__':
    main()