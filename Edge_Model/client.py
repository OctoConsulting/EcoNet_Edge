from flask import Flask, request, jsonify
from flask_sock import Sock
import os, json, subprocess, shutil
import base64
import librosa
from librosa import onset
import wave
from pydub import AudioSegment

app = Flask(__name__)

@app.route('/model', methods=['POST'])
def point():
    
    body = request.json

    base64_bytes = body['audio']

    # convert from base64 to bytes
    my_bytes = base64.b64decode(base64_bytes)
    
    with wave.open('myfile.wav', 'wb') as f:
        f.setnchannels(4)
        f.setsampwidth(2)
        f.setframerate(44100)
        f.writeframes(my_bytes)

    audio, sr = librosa.load('myfile.wav')
    # this gives the onset as a timestamp in seconds
    # onsets = onset.onset_detect(y=y, sr=sr)

    print(sr, flush=True)
    
    # a = AudioSegment.from_file('myfile.wav', format='wav')

    # a = a[0:len(a)+6]


    # if onsets[0] >= 0.6:
        # trim from 0.6 to end
    # else:
    #     # trimp from onset[0] tplus 0.6 seconds
    #     a = a[onsets[0]*1000:onsets[0]*1000+0.6*1000]

    print('done', flush=True)
    # a.export('in.wav', format='wav')

    # print(librosa.get_duration(audio, sr))


    # make .wav file


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
    return jsonify(data)