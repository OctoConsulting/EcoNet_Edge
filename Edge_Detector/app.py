from flask import Flask, request, jsonify
from flask_sock import Sock
import pyaudio


app = Flask(__name__)
sock = Sock(app)

@app.route('/api/detectShot', methods=['POST'])
def detect_shot():
    if 'file' not in request.files:
        return 'No file part in the request'

    file = request.files['file']

    if file.filename == '':
        return 'No selected file'

    # send file to shot detector

    # get return and return

    resp = {
        'shot':True
    }

    return jsonify(resp)



if __name__ == '__main__':
    app.run()