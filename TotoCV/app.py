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
    # feed each chunk to be evaluated in the model

    input_data = 'image of rock'

    # Run the subprocess and wait for it to complete
    # process = subprocess.call(['python', 'toto.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    # stdout, stderr = process.communicate(input=input_data)
    # return_code = process.returncode

    args = f'python toto.py'
    result = subprocess.run(['python', 'toto.py'], capture_output=True, text=True)
    output = result.stdout
    # data = process.decode('utf-8')

    # Subprocess completed successfully
    d = {
        'x': 12,
        'y': 23,
        'object': output
    }
    return jsonify(d)
