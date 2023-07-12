from flask import Flask, request, jsonify
from flask_sock import Sock
import os, json, subprocess, shutil
import base64
import librosa
from librosa import onset
import wave

app = Flask(__name__)

@app.route('/model', methods=['POST'])
def point():
    
    body = request.json

    base64_bytes = body['audio']

    # convert from base64 to bytes
    my_bytes = base64.b64decode(base64_bytes)

    # make .wav file
    with wave.open('myfile.wav', 'wb') as f:
        f.setnchannels(4)
        f.setsampwidth(2)
        f.setframerate(96000)
        f.writeframes(my_bytes)


    subprocess_cmd = ['python', 'acoustic_inference_tf.py', 'myfile.wav']
    subprocess_output = subprocess.run(subprocess_cmd, capture_output=True, text=True)

    # Check if the subprocess succeeded
    if subprocess_output.returncode != 0:
        print(subprocess_output.stderr.strip(), flush=True)
        return jsonify({'Subprocess failed': subprocess_output.stderr.strip()}), 501
    
    # storing stdout of the subprocess to output
    output = subprocess_output.stdout.strip()
    #loading output data into json format into data
    data = json.loads(output)
    print(data, flush=True)
    # return json of data

    # data = {}

    # data['Angle'] = "0"
    # data['Distance'] = "7" 
    # data['Weapon'] = "pistol"
    # data['Azimuth'] = "225"

    return jsonify(data)
