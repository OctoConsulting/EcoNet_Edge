from flask import Flask, request, jsonify
from flask_sock import Sock
import os, json, subprocess, shutil

app = Flask(__name__)

@app.route('/model', methods=['POST'])
def point():
    # Check if the request contains a file
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    
    # Check if the file has a valid extension
    if file.filename == '' or not file.filename.endswith('.wav'):
        return jsonify({'error': 'Invalid file type'}), 400
    
    # Save the WAV file
    wav_path = 'input.wav'
    subprocess_cmd = ['python', 'Edge_Model_Main.py', wav_path]
    subprocess_output = subprocess.run(subprocess_cmd, capture_output=True, text=True)
    # storing stdout of the subprocess to output
    output = subprocess_output.stdout.strip()
    #loading output data into json format into data
    data = json.loads(output)
    # return json of data
    return jsonify(data)