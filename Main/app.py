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
import logging

# lots of unnecessary stuff to console
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

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

            current_time= datetime.now(timezone('America/New_York')).strftime("%H-%M-%S")
            print(f'shot time: [{time}] eval time: [{current_time}] {resp_json} (shot detector)', flush=True)
            
            if resp_json["shot"]:
                # db and video stuff
                shot_data= {'preprocessed_audio_hash': "UNIMPLEMENTED"}
                json_headers= {'Content-Type': 'application/json'}
                db_return= requests.post(f'http://db_courier:5000/post_shot_raw',
                          data = shot_data,
                          headers = json_headers)
                db_index= db_return.json()['index']
                print("The index of the inputted shot is: ", db_index)
                # video
                status= requests.get('http://encode:5000/start_drone1')
                print("The Drone Status is...", status.json(), flush= True)

                # Define the command and arguments
                command = ["python", "locate.py", str(db_index), str(time)]

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
