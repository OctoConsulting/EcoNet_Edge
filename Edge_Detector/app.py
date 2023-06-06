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
    result = subprocess.Popen(['python', 'detector_out.py'], stdout=subprocess.PIPE)
    result.wait()
    stdout = result.stdout

    # get return and return
    shot = False
    if stdout == 1:
        shot = True

    resp = {
        'shot':shot
    }


    return jsonify(resp)
        