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

            shot = response.json()

            if shot:
                # run preprossing
                # store in a file
                # maybe use subporssess or fork+exec

                os.fork()
                PID_AFTER_FORK = os.getpid()
                if PID_AFTER_FORK != PARENT_PID:
                    # might need pipe to send data from current to model and deployment code
                    program_path = 'locate_and_deploy'
                    os.execlp('python3', 'python3', program_path)
                        
    except (KeyboardInterrupt, EOFError, simple_websocket.ConnectionClosed):
        ws.close()


if __name__ == '__main__':
    main()