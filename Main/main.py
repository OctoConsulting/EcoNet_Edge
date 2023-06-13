import simple_websocket
import os
import sys
import requests
import base64


def main():
    PARENT_PID = os.getpid()
    # url = '172.18.0.2:5000/api'
    url = 'api:5000/api'

    ws = simple_websocket.Client(f'ws://{url}/detection/audio')
    # ws = simple_websocket.Client(f'ws://{url}/detection/audio')
    try:
        while True:
            byte_array = ws.receive()
            base64_bytes = base64.b64encode(byte_array)
            
            a = {}
            a['audio'] = base64_bytes.decode('utf-8')

            response = requests.post(f'http://{url}/detection/detectShot', json=a)

            resp_json = response.json()
            shot = resp_json.get('shot')
            audio = resp_json.get('audio')

            if shot:
                # run preprossing
                # store in a file
                # maybe use subporssess or fork+exec

                os.fork()
                PID_AFTER_FORK = os.getpid()
                if PID_AFTER_FORK != PARENT_PID:
                    program_path = 'locate_and_deploy'
                    os.execlp('python3', program_path, audio)
                        
    except (KeyboardInterrupt, EOFError, simple_websocket.ConnectionClosed):
        ws.close()


if __name__ == '__main__':
    main()