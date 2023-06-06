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
    # get drone feed through websocket
    # feed each chucnk to be evaluteed in model

    input_data='image of rock'
    result = subprocess.run(['python', 'toto.py'], capture_output=True, text=True, input=input_data)
    stdout = result.stdout

    data = {
        'x':12,
        'y':23,
        'object':stdout
    }

    return jsonify(data)