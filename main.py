import simple_websocket
import os
import sys
import requests


def main():
    PARENT_PID = os.getpid()
    # url = '172.18.0.2:5000/api'
    url = '172.18.0.2:5000/api'

    ws = simple_websocket.Client(f'ws://{url}/detection/audio')
    # ws = simple_websocket.Client(f'ws://{url}/detection/audio')
    try:
        while True:
            byte_array = ws.receive()
            # take data an feed into shot detector
            # if data has shot 
                # fork and exec to new prossess

            file_path = './temp.txt'  # Path to the file you want to upload

            # Send the audio chunk file through a POST request to detector
            file = open(file_path, 'wb+')
            file.write(byte_array)
            response = requests.post(f'http://{url}/detection/detectShot', files={'file': file})

            print(response)
            # file.write(str(response))

            shot = response

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
            
            file.close()
            
    except (KeyboardInterrupt, EOFError, simple_websocket.ConnectionClosed):
        ws.close()


if __name__ == '__main__':
    main()