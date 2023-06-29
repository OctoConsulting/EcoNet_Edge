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

@app.route('/video/start_drone1', methods=['GET'])
def drone1_start():
    return jsonify(controls.start_drone(1).name)

@app.route('/video/stop_drone1', methods=['GET'])
def drone1_stop():
    return jsonify(controls.stop_drone(1).name)

@app.route('/video/start_drone2', methods=['GET'])
def drone2_start():
    return jsonify("UNIMPLEMENTED")

@app.route('/video/stop_drone2', methods=['GET'])
def drone2_stop():
    return jsonify("UNIMPLEMENTED")

@app.route('/video/start_drone3', methods=['GET'])
def drone3_start():
    return jsonify("UNIMPLEMENTED")

@app.route('/video/stop_drone3', methods=['GET'])
def drone3_stop():
    return jsonify("UNIMPLEMENTED")

if __name__ == '__main__':
    app.run()