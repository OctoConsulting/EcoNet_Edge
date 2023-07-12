import wave
from flask import Flask, request, jsonify, send_file
from flask_sock import Sock
import requests, json
import simple_websocket
import subprocess
import base64
import wave
import pyaudio
from datetime import datetime, timedelta
from pytz import timezone

app = Flask(__name__)
sock = Sock(app)

@sock.route('/api/detection/audio', methods=['GET'])
def get_audio(ws):
    url = 'api:5000/api'

    start_time = datetime.now(timezone('America/New_York')).strftime("%H-%M-%S")
    #f = open(f"../logs/start-{start_time}", "x")
    
    try:
        while True:
            byte_array = ws.receive()
            time= ws.receive()
            base64_bytes = base64.b64encode(byte_array)
            #now = datetime.now(timezone('America/New_York'))
            #offset= now + timedelta(seconds= -4)
            #time= offset.strftime("%H-%M-%S")
            
            a = {}
            a['audio'] = base64_bytes.decode('utf-8')
            
            response = requests.post(f'http://{url}/detection/detectShot', json=a)

            resp_json = response.json()
            print(f'[{time}] {resp_json} (shot detector)', flush=True)
            
            if resp_json["shot"]:
                # Define the command and arguments
                command = ["python", "locate.py", "db_index", str(time)]

                # Launch the subprocess and redirect stdout to a pipe
                process = subprocess.Popen(command, stdin=subprocess.PIPE)

                # Send data to the subprocess
                data = json.dumps(a['audio']).encode("utf-8")  # Encode the string as bytes
                process.stdin.write(data)
                process.stdin.close()                    

                        
    except (KeyboardInterrupt, EOFError, simple_websocket.ConnectionClosed):
        #f.close()
        ws.close()

if __name__ == '__main__':
    app.run()
