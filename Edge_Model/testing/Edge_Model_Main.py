from flask import jsonify
import json
import sys

def sphericalCoordinatesCalculator(input_wav):
    # hard coded data for dummy container
    data = {
        "theta": 90,
        "phi": 45,
        "r": 5.5
    }
    # returning a json format of the data
    return json.dumps(data)

if __name__ == '__main__':
    #takes in argument from client.py
    input_wav = sys.argv[1]
    #sends the argument back into stdout to be read by mian
    sys.stdout.write(sphericalCoordinatesCalculator(input_wav))