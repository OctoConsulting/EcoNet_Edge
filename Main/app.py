import wave
from flask import Flask, request, jsonify, send_file
from flask_sock import Sock
import requests, json
import simple_websocket
import subprocess
import base64
import wave
import pyaudio


app = Flask(__name__)
sock = Sock(app)

@sock.route('/api/detection/audio', methods=['GET'])
def get_audio(ws):
    url = 'api:5000/api'
    
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
                shot_data= {'preprocessed_audio_hash': "UNIMPLEMENTED"}
                json_headers= {'Content-Type': 'application/json'}
                db_index= requests.post(f'http://db_courier:5000/post_shot_raw',
                                        data= shot_data,
                                        headers= json_headers)
                # Define the command and arguments
                command = ["python", "locate.py", str(db_index)]

                # Launch the subprocess and redirect stdout to a pipe
                process = subprocess.Popen(command, stdin=subprocess.PIPE)

                # Send data to the subprocess
                data = json.dumps(a['audio']).encode("utf-8")  # Encode the string as bytes
                process.stdin.write(data)
                process.stdin.close() 
 
    except (KeyboardInterrupt, EOFError, simple_websocket.ConnectionClosed):
        ws.close()

if __name__ == '__main__':
    app.run()
