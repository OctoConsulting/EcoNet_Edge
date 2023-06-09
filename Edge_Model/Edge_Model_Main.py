from flask import jsonify
import json
import sys

def main():
    global data 
    data = {
        "theta": 90,
        "phi": 45,
        "r": 5.5
    }
    try:
        with open('output.json', 'w') as file:
            json.dump(data, file)
    except Exception as e:
        print(f"Error writing to file: {str(e)}")
    return json.dumps(data)

if __name__ == '__main__':
    sys.stdout.write(main())