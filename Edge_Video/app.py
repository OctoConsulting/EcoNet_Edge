from flask import Flask, request, jsonify
from flask_sock import Sock
import requests
from flask_cors import CORS
import controls

app = Flask(__name__)
CORS(app)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

sock = Sock(app)

@app.route('/', methods=['GET'])
def default():
    return jsonify("heyy :)")

@app.route('/video/drone1_start', methods=['GET'])
def drone1_start():
    return jsonify(controls.start_drone(1))

@app.route('/video/drone1_stop', methods=['GET'])
def drone1_stop():
    return jsonify("heyy :)")

if __name__ == '__main__':
    app.run()