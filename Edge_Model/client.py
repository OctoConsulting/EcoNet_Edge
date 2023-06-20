from flask import Flask, request, jsonify
from flask_sock import Sock
import os, json, subprocess, shutil
import base64

app = Flask(__name__)

@app.route('/model', methods=['POST'])
def point():
    
    body = request.json

    base64_bytes = body['audio']

    # convert from base64 to bytes
    my_bytes = base64.b64decode(base64_bytes)

    # make .wav file
    with open('myfile.wav', mode='wb') as f:
        f.write(my_bytes)

    subprocess_cmd = ['python', 'Edge_Model_Main.py', 'myfile.wav']
    subprocess_output = subprocess.run(subprocess_cmd, capture_output=True, text=True)

    # Check if the subprocess succeeded
    if subprocess_output.returncode != 0:
        return jsonify({'Subprocess failed': subprocess_output.stderr.strip()}), 501
    
    # storing stdout of the subprocess to output
    output = subprocess_output.stdout.strip()
    #loading output data into json format into data
    data = json.loads(output)
    # return json of data
    return jsonify(data)