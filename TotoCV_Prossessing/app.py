import simple_websocket
import json

def search_for_people(array_of_dicts):
    for dictionary in array_of_dicts:
        if 'person' in dictionary.values():
            return True
    return False

def main(drone_ip):
    # TODO change this to toto docker ip
    url = 'toto:5000'
    # TODO change the end point to match the flask app
    ws = simple_websocket.Client(f'ws://{url}/toto/{drone_ip}')

    count = 0
    treshold = 200

    try:
        while True:
            data = ws.receive()

            # do something with the data
            data_loaded = json.loads(data)
            arr = data_loaded['detections']

            # what if there are multiple people in the frame
            if search_for_people(arr):
                count += 1
                if count >= treshold:
                    # save image --> writing to database
                    # send actions to drone protocal
                    pass
            else:
                count = 0
            
 
    
    except (KeyboardInterrupt, EOFError, simple_websocket.ConnectionClosed):
        ws.close()


if __name__ == '__main__':
    main()