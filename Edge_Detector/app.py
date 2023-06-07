from flask import Flask, request, jsonify
from flask_sock import Sock
import subprocess


app = Flask(__name__)
sock = Sock(app)

@app.route('/api/detectShot', methods=['POST'])
def detect_shot():
    #file = request.files['file']

    #if 'file' not in request.files:
   #     return 'No file part in the request'

    #if file.filename == '':
   #     return 'No selected file'
    # send file to shot detector

    result = subprocess.run(['python', '-c', 'import random; print(random.randint(0, 1))'], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8').strip()
    random_number = int(output)

    # result = subprocess.run(['python', 'detector_out.py'], stdout=subprocess.PIPE)
    # temp = result.stdout.decode('utf-8').strip()
    # print(temp)

    # get return and return
    shot = False
    if random_number == 1:
        shot = True

    resp = {
        'shot':shot
    }

    return jsonify(resp)
        