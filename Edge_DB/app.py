from flask import Flask, request, jsonify
from flask_sock import Sock
import requests
import query_get
import query_put
import query_post
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

sock = Sock(app)

# test websocket endpoint # @sock.route for web sockets
#@sock.route('/api/test', methods=['GET']) # route(path endpoint, {GET, POST, PUT, DELETE})
#def test(ws): # ws for websocket
#    while True:
#        ws.send("hello world") # only can send text & bytearr

# hello
@app.route('/', methods=['GET'])
def default():
    return jsonify("heyy :)")
# gets all shots
@app.route('/db/get_all_shots', methods=['GET'])
def get_all_shots():
    return jsonify(query_get.get_all_shots())

# gets all shot_stats
@app.route('/db/get_all_shot_stats', methods=['GET'])
def get_all_shot_stats():
    return jsonify(query_get.get_all_shot_stats())

# gets all events
@app.route('/db/get_all_events', methods=['GET'])
def get_all_events():
    return jsonify(query_get.get_all_events())

# gets all markers
@app.route('/db/get_all_markers', methods=['GET'])
def get_all_markers():
    return jsonify(query_get.get_all_markers())

# gets all events
#@app.route('/db/get_all_shots_for_event', methods=['GET'])
#def get_all_shots_for_event():
#    hash= request.args.get('id')
#    return jsonify(query_get.get_all_events())

# gets a shot by the preprocessed hash
@app.route('/db/get_shot_by_pre', methods=['GET'])
def get_shot_by_pre():
    hash= request.args.get('hash')
    hash= "\'" + hash + "\'"
    return jsonify(query_get.get_all_where("shots", "preprocessed_audio_hash", "ILIKE", hash)[0])

# gets a shot by the id
@app.route('/db/get_shot_by_id', methods=['GET'])
def get_shot_by_id():
    id= request.args.get('id')
    return jsonify(query_get.get_all_where("shots", "id", "=", id)[0])

# gets a shot's statistics by id
@app.route('/db/get_shot_stats_by_id', methods=['GET'])
def get_shot_stats_by_id():
    id= request.args.get('id')
    return jsonify(query_get.get_all_where("shot_stats", "id", "=", id)[0])


@app.route('/db/put_shot_raw', methods=['POST'])
def put_shot_raw():
#    shot_time= request.args.get('shot_time')
#    preprocessed_audio_hash= request.args.get('preprocessed_audio_hash')
#    return jsonify(query_get.put_shot_raw(shot_time, preprocessed_audio_hash))
    return jsonify("UNIMPLEMENTED")

@app.route('/db/update_marker_db/<string:id>', methods=['PUT'])
def update_marker_db(id):
    # Retrieve the data from the request body
    query_put.put_marker(request.json, id)
    
    # Return a response indicating the success of the operation
    return jsonify({'message': f'Marker with ID {id} updated successfully'})

@app.route('/db/post_marker_db', methods=['POST'])
def post_marker_db():
    # Retrieve the data from the request body
    query_post.post_marker(request.json)
    
    # Return a response indicating the success of the operation
    return jsonify({'message': f'Marker inserted successfully'})


@app.route('/db/put_shot_detector_model', methods=['PUT'])
def put_shot_detector_model():
    return jsonify("UNIMPLEMENTED")

@app.route('/db/put_shot_acoustic_model', methods=['PUT'])
def put_shot_acoustic_model():
    return jsonify("UNIMPLEMENTED")

@app.route('/db/put_shot_drone_mission', methods=['PUT'])
def put_shot_drone_mission():
    return jsonify("UNIMPLEMENTED")

if __name__ == '__main__':
    app.run()