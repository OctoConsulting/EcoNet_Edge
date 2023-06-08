from flask import Flask, request, jsonify
from flask_sock import Sock
import os
import subprocess
import json

app = Flask(__name__)

@app.route('/model', methods=['POST'])
def point():
    subprocess_output = subprocess.run(['python', 'Edge_Model_Main.py'], capture_output=True, text=True)
    output = subprocess_output.stdout.strip()
    data = json.loads(output)
    return jsonify(data)