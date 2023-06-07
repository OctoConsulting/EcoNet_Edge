from flask import Flask, request, jsonify
from flask_sock import Sock
import os

# this is localhost:8000

app = Flask(__name__)
sock = Sock(app)

@app.route('/model', methods=['POST'])
def point():
    
    theta = 90
    phi = 45
    r = 5.5

    data = {
        'theta': theta,
        'phi': phi,
        'r': r,
    }

    return jsonify(data)