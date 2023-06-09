from flask import Flask, request, jsonify
from flask_sock import Sock
import requests
import get_queries
import put_queries

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

sock = Sock(app)

# test websocket endpoint # @sock.route for web sockets
#@sock.route('/api/test', methods=['GET']) # route(path endpoint, {GET, POST, PUT, DELETE})
#def test(ws): # ws for websocket
#    while True:
#        ws.send("hello world") # only can send text & bytearr

# gets all shots
@app.route('/db/get_all_shots', methods=['GET'])
def get_all_shots():
    return jsonify(get_queries.get_all_from("shots"))

# gets all events
@app.route('/db/get_all_events', methods=['GET'])
def get_all_events():
    return jsonify(get_queries.get_all_from("events"), compact= False)

# gets a shot by the preprocessed hash
@app.route('/db/get_shot_by_pre', methods=['GET'])
def get_shot_by_pre():
    hash= request.args.get('hash')
    hash= "\'" + hash + "\'"
    return jsonify(get_queries.get_all_where("shots", "preprocessed_audio_hash", "ILIKE", hash)[0])

# gets a shot by the id
@app.route('/db/get_shot_by_id', methods=['GET'])
def get_shot_by_id():
    id= request.args.get('id')
    return jsonify(get_queries.get_all_where("shots", "id", "=", id)[0])

@app.route('/db/put_shot_raw', methods=['POST'])
def put_shot_raw():
    shot_time= request.args.get('shot_time')
    preprocessed_audio_hash= request.args.get('preprocessed_audio_hash')
    return jsonify(put_queries.put_shot_raw(shot_time, preprocessed_audio_hash))

@app.route('/db/put_shot_detector_model', methods=['PUT'])
def put_shot_detector_model():
    print("UNIMPLEMENTED")

@app.route('/db/put_shot_acoustic_model', methods=['PUT'])
def put_shot_acoustic_model():
    print("UNIMPLEMENTED")

@app.route('/db/put_shot_drone_mission', methods=['PUT'])
def put_shot_drone_mission():
    print("UNIMPLEMENTED")

if __name__ == '__main__':
    app.run()