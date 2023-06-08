import json
import sys

def main():
    data = {
        "theta": 90,
        "phi": 45,
        "r": 5.5
    }
    return json.dumps(data)

if __name__ == '__main__':
    print(main())