from flask import jsonify
import json
import sys

def main():
    # hard coded data for dummy container
    data = {
        "theta": 90,
        "phi": 45,
        "r": 5.5
    }
    # returning a json format of the data
    return json.dumps(data)

if __name__ == '__main__':
    sys.stdout.write(main())