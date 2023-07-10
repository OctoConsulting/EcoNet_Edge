import os
import sys
import json 
import requests

def main():
    data = sys.argv[1]
    location = json.loads(data)

    print(str(location), flush=True)

    url ='http://Manager:5000'

    # drone manager
    response = requests.post(f'http://{url}/api/coordinates', json=location)
    

if __name__ == '__main__':
    main()