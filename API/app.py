from flask import Flask, request, jsonify
from flask_sock import Sock
import pyaudio
import requests

app = Flask(__name__)
sock = Sock(app)

    


# test websocket endpoint # @sock.route for web sockets
@sock.route('/api/test', methods=['GET']) # route(path endpoint, {GET, POST, PUT, DELETE})
def test(ws): # ws for websocket
    while True:
        ws.send("hello world") # only can send text & bytearr


####################################################################

# detection endpoints


@app.route('/api/preporessing', methods=['POST'])
def preprocessing():
    if 'file' not in request.files:
        return 'No file part in the request'

    file = request.files['file']

    if file.filename == '':
        return 'No selected file'

    


    url = 'http://noise:5000/convert'
    response = requests.post(url, files=file)
    return response.json()


@app.route('/api/detection', methods=['GET'])
def detactions_options():
    return '***' # return jsonify({}) <-- give them a nice json :)

@sock.route('/api/detection/audio', methods=['GET'])
def get_audio(ws):
    audio_format = pyaudio.paInt16

    channels = 1 
    sample_rate = 44100
    chunk_size = 512

    audio = pyaudio.PyAudio()

    stream = audio.open(format=audio_format, channels=channels, rate=sample_rate, input=True, frames_per_buffer=chunk_size, input_device_index=0)

    try:
        while True:
            data = stream.read(1024)
            print(data)
            print('_________________________________________')
            ws.send(data)

        
    except KeyboardInterrupt:
            pass
    stream.stop_stream()
    stream.close()
    audio.terminate()

@app.route('/api/detection/detectShot', methods=['POST'])
def detect_shot():
    if 'file' not in request.files:
        return 'No file part in the request'

    file = request.files['file']

    if file.filename == '':
        return 'No selected file'

    # send file to shot detector
    # get return and return

    resp = {
        'shot':True
    }

    return jsonify(resp)

@app.route('/api/detection/getLocation', methods=['POST'])
def get_location():
    if 'file' not in request.files:
        return 'No file part in the request'

    file = request.files['file']

    if file.filename == '':
        return 'No selected file'

    # noice redection
    
    # send file to audio madel

    # return value

    return 'File uploaded successfully'


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
    url = 'http://toto:5000/toto'
    response = requests.post(url)

    with open('output.txt', 'w') as file:
        file.write(str(response.json()))

    return response.json()


# surge endpoints
@app.route('/api/surge', methods=['GET'])
def surge_options():
    return 'surge_options'


# cloud endpoints





if __name__ == '__main__':
    app.run()
