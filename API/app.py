from flask import Flask, request, jsonify
from flask_sock import Sock
import pyaudio
import requests, json

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
# Check if the request contains a file
    if 'file' not in request.files:
        return 'No file uploaded', 400
    
    file = request.files['file']

    # Get the specified parameter from the request
    param_value = request.form.get('param')

    # Save the WAV file to a temporary location
    file.save('input.wav')

    # Send a request to B.py with the WAV file
    response = requests.post('http://noise:5000/process_wav', files={'file': open('input.wav', 'rb')}, data={'param': param_value})

    if response.status_code == 200:
        # Retrieve the processed WAV file from B.py
        processed_file = response.content

        # Save the processed WAV file
        with open('processed.wav', 'wb') as f:
            f.write(processed_file)

        return 'WAV file processed successfully'
    else:
        return 'Failed to process WAV file'



@app.route('/api/detection', methods=['GET'])
def detactions_options():
    return '***' # return jsonify({}) <-- give them a nice json :)

@sock.route('/api/detection/audio', methods=['GET'])
def get_audio(ws):
    audio_format = pyaudio.paInt16

    channels = 1 
    sample_rate = 44100
    chunk_size = 1000000

    audio = pyaudio.PyAudio()

    stream = audio.open(format=audio_format, channels=channels, rate=sample_rate, input=True, frames_per_buffer=chunk_size)

    try:
        while True:
            data = stream.read(1024)
            print('data')
            print('_________________________________________')
            ws.send(data)

        
    except KeyboardInterrupt:
            pass
    stream.stop_stream()
    stream.close()
    audio.terminate()

@app.route('/api/detection/detectShot', methods=['POST'])
def detect_shot():
    # if 'file' not in request.files:
    #     return 'No file part in the request'

    # file = request.files['file']

    # if file.filename == '':
    #     return 'No selected file'

    url = 'http://shot_detect:5000/api/detectShot'
    response = requests.post(url)

    return response.json()

@app.route('/api/getLocation', methods=['POST'])
def get_location():
    url = 'http://model:5000/model'
    response = requests.post(url)

    # Extract the response data as JSON
    response_data = response.json()

    # Write the JSON data to a file
    try:
        with open('output.json', 'w') as file:
            json.dump(response_data, file)
    except Exception as e:
        print(f"Error writing to file: {str(e)}")
    return jsonify(response_data)

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
