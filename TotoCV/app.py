from flask import Flask, request, jsonify
from flask_sock import Sock
import toto
import os
import subprocess

# this is localhost:8000

app = Flask(__name__)
sock = Sock(app)

@app.route('/toto', methods=['POST'])
def point():

    result = subprocess.run(['python', 'toto/main.py', '../cat.jpeg'], capture_output=True, text=True)
    output = result.stdout

    d = {
        'x': 12,
        'y': 23,
        'object': output
    }
    
    return jsonify(d)
