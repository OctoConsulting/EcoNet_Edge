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
    return jsonify("heyy ;), ur in encode rn :)")

@app.route('/start_test', methods=['GET'])
def start_test():
    return jsonify(controls.start_test().name)

@app.route('/stop_test', methods=['GET'])
def stop_test():
    return jsonify(controls.stop_test().name)

@app.route('/start_drone1', methods=['GET'])
def start_drone1():
    return jsonify(controls.start_drone(1).name)

@app.route('/stop_drone1', methods=['GET'])
def stop_drone1():
    return jsonify(controls.stop_drone(1).name)

# for field day, we are only using one drone. Will create new containers for
# each of the other drones
@app.route('/start_drone2', methods=['GET'])
def start_drone2():
    return jsonify("UNIMPLEMENTED")

@app.route('/stop_drone2', methods=['GET'])
def stop_drone2():
    return jsonify("UNIMPLEMENTED")

@app.route('/start_drone3', methods=['GET'])
def start_drone3():
    return jsonify("UNIMPLEMENTED")

@app.route('/stop_drone3', methods=['GET'])
def stop_drone3():
    return jsonify("UNIMPLEMENTED")

if __name__ == '__main__':
    app.run()