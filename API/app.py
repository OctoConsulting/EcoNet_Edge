# api app.py

import wave
from flask import Flask, request, jsonify, send_file
from flask_sock import Sock
import pyaudio
import requests, json
import simple_websocket
import subprocess
import base64
import wave
import pyaudio


app = Flask(__name__)
sock = Sock(app)


#################################
# get audio from mic
#################################
@sock.route('/api/detection/audio', methods=['GET'])
def get_audio(ws):
    #try:
    
    #    url = '192.168.50.100:5000'
    #    w_out = simple_websocket.Client(f'ws://{url}/audio')
    #    while True:
    #        data = w_out.receive()
    #        ws.send(data)
            
    #except KeyboardInterrupt:
    #    pass
    
    try:
        while True:
            byte_array = ws.receive()
            base64_bytes = base64.b64encode(byte_array)
            
            a = {}
            a['audio'] = base64_bytes.decode('utf-8')
            audio= pyaudio.PyAudio()
            #with file.open('heyy', 'w') as file:
            with wave.open(f"audio[i].wav", "wb") as wf:
                wf.setnchannels(4)
                wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
                wf.setframerate(44100)
                wf.writeframes(byte_array)
            #print(a, flush= True)
            #response = requests.post(f'http://{url}/detection/detectShot', json=a)

            #resp_json = response.json()
            #shot = resp_json.get('shot')

            #if shot:
                # Define the command and arguments
            #    command = ["python", "locate.py"]

                # Launch the subprocess and redirect stdout to a pipe
            #    process = subprocess.Popen(command, stdin=subprocess.PIPE)

                # Send data to the subprocess
            #    data = json.dumps(a['audio']).encode("utf-8")  # Encode the string as bytes
            #    process.stdin.write(data)
            #    process.stdin.close() 
                    

                        
    except (KeyboardInterrupt, EOFError, simple_websocket.ConnectionClosed):
        ws.close()



#################################
# detect shot from audio
#################################
@app.route('/api/detection/detectShot', methods=['POST'])
def detect_shot():
    body = request.json

    headers = {'Content-Type': 'application/json'}

    response = requests.post('http://shot_detect:5000/api/detectShot', json=body, headers=headers)

    if response.status_code == 200:
        return response.json()
    
    else:
        return 'Failed Shot Detection'
    

#################################
# preporess audio
#################################
@app.route('/api/preporessing', methods=['POST'])
def preprocessing():
    body = request.json

    headers = {'Content-Type': 'application/json'}

    response = requests.post('http://noise:5000/process_wav', json=body, headers=headers)

    return response.json()


#################################
# get loacation of gunshot
#################################
@app.route('/api/getLocation', methods=['POST'])
def get_location():
    body = request.json

    headers = {'Content-Type': 'application/json'}

    response = requests.post('http://model:5000/model', json=body, headers=headers)

    if response.status_code == 200:
        return response.json()
    
    else:
        return 'Failed get location'





# drone endpoints
@app.route('/api/drone', methods=['GET'])
def drone_options():
    return 'drone_options'

@app.route('/api/drone/chooseDrone', methods=['POST'])
def choose_drone():
    return 'choose_drone'

@app.route('/api/drone/sendDrone', methods=['POST'])
def send_drone():
    return 'send_drone'


# TOTO CV endpoints
@sock.route('/api/toto', methods=['GET'])
def toto_options(ws):
    while True:
        data = ws.receive()
        ws.send(data[::-1])

# this is localhost:9000
@app.route('/api/toto/getObjects', methods=['POST'])
def get_objects():
    
    # url = 'http://172.19.0.2:5000/toto'
    url = 'http://totocv:5000/toto'
    response = requests.post(url)

    # with open('output.txt', 'w') as file:
    #     file.write(str(response.json()))

    return response.json()


# surge endpoints
@app.route('/api/surge', methods=['GET'])
def surge_options():
    return 'surge_options'


# cloud endpoints





if __name__ == '__main__':
    app.run()
