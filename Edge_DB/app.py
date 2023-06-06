from flask import Flask, request, jsonify
from flask_sock import Sock
import requests
import select_queries

app = Flask(__name__)
sock = Sock(app)

# test websocket endpoint # @sock.route for web sockets
#@sock.route('/api/test', methods=['GET']) # route(path endpoint, {GET, POST, PUT, DELETE})
#def test(ws): # ws for websocket
#    while True:
#        ws.send("hello world") # only can send text & bytearr

@app.route('/api/get_all_shots', methods=['GET'])
def get_all_shots():
    return jsonify(select_queries.get_all_shots())

@app.route('/api/get_all_events', methods=['GET'])
def get_all_events():
    return jsonify(select_queries.get_all_events())

if __name__ == '__main__':
    app.run()
