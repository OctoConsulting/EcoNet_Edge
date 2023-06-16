from flask import Flask, request, jsonify
from flask_sock import Sock
import toto
import os
import subprocess
from toto import main

# this is localhost:8000

app = Flask(__name__)
sock = Sock(app)

@app.route('/toto', methods=['POST'])
def point():

    # how are we getting the ip adress of the drone
    body = request.json
    drone_ip = body['drone_ip']
    
    live = 'rtsp://' + drone_ip + '/live'

    main(live)
    
    return
