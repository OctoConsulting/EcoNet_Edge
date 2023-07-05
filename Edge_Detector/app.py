from flask import Flask, request, jsonify
import subprocess
import os
import json
import base64

app = Flask(__name__)

@app.route('/api/detectShot', methods=['POST'])
def detect_shot():

        body = request.json

        base64_bytes = body['audio']

        # convert from base64 to bytes
        my_bytes = base64.b64decode(base64_bytes)

        # make .wav file
        with open('myfile.wav', mode='wb') as f:
                f.write(my_bytes)

        subprocess_cmd = ['python', './testing/detector_out.py', 'myfile.wav']
        subprocess_output = subprocess.run(subprocess_cmd, capture_output=True, text=True)
        
        # Check if the subprocess succeeded
        if subprocess_output.returncode != 0:
                return jsonify({'Subprocess failed': subprocess_output.stderr.strip()}), 501

        output = subprocess_output.stdout.strip()
        json_output = json.loads(output)

        resp = {}
        resp['shot'] = json_output['shot']

        # with open(json_output['audio'], 'rb') as fd:
        #         contents = fd.read()
        #         resp['audio'] = convert_to_base64(contents)
        
        return jsonify(resp)


# this is a function that converts a byte array to base64 (this is needed to be able to send in JSON)
def convert_to_base64(byte_array):
    base64_bytes = base64.b64encode(byte_array)
    return base64_bytes.decode('utf-8')
