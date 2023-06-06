from flask import Flask, request, jsonify
from flask_sock import Sock
import requests

app = Flask(__name__)
sock = Sock(app)

# test websocket endpoint # @sock.route for web sockets
@sock.route('/api/test', methods=['GET']) # route(path endpoint, {GET, POST, PUT, DELETE})
def test(ws): # ws for websocket
    while True:
        ws.send("hello world") # only can send text & bytearr

@app.route('/api/test2', methods=['GET'])
def test2():
    return jsonify("heyy ;)")

if __name__ == '__main__':
    app.run()
