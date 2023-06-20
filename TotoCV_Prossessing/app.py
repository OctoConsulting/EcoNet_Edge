import simple_websocket
import json
import numpy as np
import requests
import math

######################################################################################
# this is a global hash table that has trackign data for each unique id
######################################################################################
tracker = {}

def search_for_people(array_of_dicts):
    for dictionary in array_of_dicts:
        if 'person' in dictionary.values():
            return True
    return False

        # detection = {}
        # detection['label'] = detect.label
        # detection['x1'] = detect.x1
        # detection['x1'] = detect.x2
        # detection['y1'] = detect.y1
        # detection['y2'] = detect.y2
        # detection['image'] = image
        # detection['id'] = id'

        # history = {}
        # history['gun'] = True
        # history['bounds'] = (x1,x2,y1,y2) <-- most recent is at the end of the array
        # histroy['record'] = [(x, y, 0),(x, y, distance from pervios center), (x, y, distance from pervios center)] <-- most recent is at the end of the array
        # history['count'] = 0
        # history['error_tolorence'] = 2 <-- this means that if there are two bad reading ins in a row then stop following object
        # history['lock'] = True <-- if True, then we want to follow this person
        # history['strikes']

def track(detection, history):
    # if the detection is too far away from the last detection then remove history from tracker
    # find center for current
    center_x = (detection['x1'] + detection['x2']) / 2
    center_y = (detection['y1'] + detection['y2']) / 2

    # finding the bounds
    width = (detection['x2'] + detection['x1'])
    height = (detection['y2'] + detection['y1'])
    side_length = min(width, height) / 2
    square_x1 = center_x - side_length
    square_x2 = center_x + side_length
    square_y1 = center_y - side_length
    square_y2 = center_y + side_length

    # if history is empty, log entry
    if len(history) == 0:
        history['gun'] = True
        history['bounds'] = (square_x1, square_x2, square_y1, square_y2)
        history['record'] = [(center_x, center_y, 0)]
        history['count'] = 0
        history['error_tolorence'] = 0 
        history['lock'] = True 
        history['strikes'] = 0
        return True

    # not a new History
    entry_bounds = history['bounds'][-1]
    x1 = entry_bounds[0]
    x2 = entry_bounds[1]
    y1 = entry_bounds[2]
    y2 = entry_bounds[3]

    entry_record = history['record'][-1]
    x = entry_record[0]
    y = entry_record[1]

    distance = math.sqrt((center_x - x) * 2 + (center_y - y) * 2)

    # if this new center in range(range is the bounds)
        # just do normal stuff
    if x1 <= center_x <= x2 and y1 <= center_y <= y2:
        new_entry = (center_x, center_x, distance)
        history['record'].append(new_entry)
        new_bounds = (square_x1, square_x2, square_y1, square_y2)
        history['bounds'] = new_bounds
        history['strikes'] = 0
        history['count'] += 1
        return True

    else:

        # if not in range and 3 strikes or more
            # throw out detection
        if history['strikes'] >= 3:
            tracker.pop(detection['id'])

        else:
            # if not in range and less than 3 strikes
            # mark down that this strike one
            history['strikes'] += 1
        return False

def createBody_protocal(history):
    body = {}
    body['center'] = history['center']

    return body

def createBody_image(detection):
    body = {}
    body['image'] = detection['image']

    return body

def main(drone_ip):
    url = 'toto:5000'
    ws = simple_websocket.Client(f'ws://{url}/toto/{drone_ip}')

    treshold = 60

    try:
        while True:
            data = ws.receive()

            # do something with the data
            data_loaded = json.loads(data)
            arr = data_loaded['detections']

            for detection in arr:
                history = tracker.get(detection[id], {})
                if detection['lable'] == 'person' and track(detection, history):
                    
                    # if we have determined that the object should be tracked and has met the minimum apperncae treshhold, then act on this
                    if history['lock'] and history['count'] >= treshold:
                        # save image --> writing to database
                        # body_image = createBody_image(detection)
                        # url_send_image = 'http://'
                        # requests.post(url_send_image, json=body_image)

                        # send actions to drone protocal
                        # body_protocal = createBody_protocal(history)
                        # url_send_to_protocal = 'http://'
                        # requests.post(url_send_to_protocal, json=body_protocal)
                        print(history['record'][-1])

                else:
                    count = 0
            
 
    
    except (KeyboardInterrupt, EOFError, simple_websocket.ConnectionClosed):
        ws.close()


if __name__ == '__main__':
    main('192.168.53.1')