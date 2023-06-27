import wave
from flask import Flask, request, jsonify, send_file
from flask_sock import Sock
import pyaudio
import requests, json
import simple_websocket

app = Flask(__name__)
sock = Sock(app)


#################################
# get audio from mic
#################################
@sock.route('/api/detection/audio', methods=['GET'])
def get_audio(ws):
    audio_format = pyaudio.paInt16

    channels = 1
    sample_rate = 44100
    # this is in bytes
    # chunk_size = 65536
    # 52920
    chunk_size = 52920*10000

    audio = pyaudio.PyAudio()

    stream = audio.open(format=audio_format, channels=channels, rate=sample_rate, input=True, frames_per_buffer=chunk_size)

    try:
        i = 0
        while True:
            data = stream.read(52920)
            ws.send(data)
            
            # wf = wave.open(f"audio{i}.wav", 'wb')
            # wf.setnchannels(channels)
            # wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
            # wf.setframerate(44100)
            # wf.writeframes(data)

            # duration_seconds = wf.getnframes() / wf.getframerate()
            # print(duration_seconds)
            # wf.close
            # i += 1
        
    except KeyboardInterrupt:
        pass
    stream.stop_stream()
    stream.close()
    audio.terminate()


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
