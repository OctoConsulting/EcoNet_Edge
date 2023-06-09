from flask import Flask, request, jsonify
from flask_sock import Sock
import os, json, subprocess, shutil

app = Flask(__name__)

@app.route('/model', methods=['POST'])
def point():
    # starting and storing into subprocess_output
    subprocess_output = subprocess.run(['python', 'Edge_Model_Main.py'], capture_output=True, text=True)
    # storing stdout of the subprocess to output
    output = subprocess_output.stdout.strip()
    #loading output data into json format into data
    data = json.loads(output)
    # return json of data
    return jsonify(data)