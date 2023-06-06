from flask import Flask, request, jsonify
from flask_sock import Sock
import subprocess


app = Flask(__name__)
sock = Sock(app)

@app.route('/api/detectShot', methods=['POST'])
def detect_shot():
    file = request.files['file']

    if 'file' not in request.files:
        return 'No file part in the request'

    if file.filename == '':
        return 'No selected file'

    # send file to shot detector
    result = subprocess.Popen(['python', 'detector_out'], stdout=subprocess.PIPE)
    stdout = result.stdout

    # get return and return

    resp = {
        'shot':True
    }

    noResp = {
        'no shot':False
    }

    if stdout == 1:
        return jsonify(resp)
    else:
        return jsonify(noResp)
        



if __name__ == '__main__':
    app.run()