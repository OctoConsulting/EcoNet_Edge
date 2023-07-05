from flask import Flask, request, jsonify
from flask_sock import Sock
import toto
import os
import subprocess
import json
import warnings
warnings.filterwarnings("ignore")
from tqdm import tqdm
from toto.yolo_inference.yolo_inference_engine import YoloInferenceEngine
from toto.bh_runner.decode_stream import *
from toto.bh_runner.klv_validation import *
import cv2
import base64
import math


# this is localhost:8000

app = Flask(__name__)
sock = Sock(app)

tracker = {0: {}}
history = {}
threshHold = 0


###########################################################
# this should manage comunication with the main porgram
###########################################################
@app.route('/toto/main', methods=['POST'])
def point():

    return

@sock.route('/toto/<drone_ip>', methods=['GET'])
def stream(ws,drone_ip=None):
    print('1', flush=True)
    if not drone_ip:
        print("error")
        return "error"
    

    try: 
        live = 'rtsp://' + drone_ip + '/live'
        frame_num = 0
        sampling_rate = 3
        conf_thresh=0.25
        weights = 'yolov5s.pt'
        print('2', flush=True)

        inf_eng = YoloInferenceEngine(weights, conf_thresh=conf_thresh)
        print('3', flush=True)
        while True:
            print('4', flush=True)
            for df in tqdm(decode_stream(live)):
                results = None
                if frame_num % sampling_rate == 0:
                    results = inf_eng.do_inference(df)
                    print('5', flush=True)
                    l = list_results(results, df)
                    display_result(results, df)

                    arr = l['detections']

                    for detection in arr:
                        # history = tracker.get(0)
                        if detection['label'] == 'person' and track(detection, history):
                            if history['count'] >= 6:
                                ws.send(history['record'][-1])
                                # print(history['record'][-1])

            frame_num += 1

    except KeyboardInterrupt:
            pass



###########################################
# this builds a dict that store the set of detections in a given frame
###########################################
def list_results(results, img):
    image = make_image(results, img)
    r = []
    for detect in results:
        e = {}
        e['label'] = detect.label
        e['x1'] = detect.x1
        e['x2'] = detect.x2
        e['y1'] = detect.y1
        e['y2'] = detect.y2
        e['image'] = image
        e['id'] = 0

        r.append(e)
    
    l = {}
    l['detections'] = r

    return l



###########################################
# this should draw a box around the object in the image and then turn that image into a byte array
# return a byte array
###########################################
def make_image(results, img):
    if results:
        for detect in results:
            # draw bounding boxes
            cv2.rectangle(img, (int(detect.x1), int(detect.y1)), (int(detect.x2), int(detect.y2)), (255, 0, 0), 1)
    
    byte_array = img.tobytes()

    return convert_to_base64(byte_array)



####################################################################################################
# this is a function that converts a byte array to base64 (this is needed to be able to send in JSON)
####################################################################################################
def convert_to_base64(byte_array):
    base64_bytes = base64.b64encode(byte_array)
    return base64_bytes.decode('utf-8')

def display_result(results, img):
    if results:
        for detect in results:

            # draw bounding boxes
            cv2.rectangle(img, (int(detect.x1), int(detect.y1)), (int(detect.x2), int(detect.y2)), (255, 0, 0), 1)
            # cv2.putText(img, str(detect.label), (int(detect.x1), int(detect.y1) + 5), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            #             fontScale=0.5, color=(0, 0, 255), thickness=1)
    
    #cv2.namedWindow("Display", cv2.WINDOW_NORMAL)
    #cv2.imshow("Display", img)
    #delay= int(1000 / 500)
    #cv2.waitKey(1)


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
    if not history:
        history['gun'] = True
        history['bounds'] = (square_x1, square_x2, square_y1, square_y2)
        history['record'] = [(center_x, center_y, 0)]
        history['count'] = 1
        history['error_tolorence'] = 0 
        history['lock'] = True 
        history['strikes'] = 0
        print("this is from history 0")
        return True

    # not a new History
    entry_bounds = history['bounds']
    x1 = entry_bounds[0]
    x2 = entry_bounds[1]
    y1 = entry_bounds[2]
    y2 = entry_bounds[3]

    entry_record = history['record'][-1]
    x = entry_record[0]
    y = entry_record[1]

    distance = math.sqrt((center_x - x) ** 2 + (center_y - y) ** 2)

    # if this new center in range(range is the bounds)
        # just do normal stuff
    if x1 <= center_x <= x2 and y1 <= center_y <= y2:
        print("i am in range!")

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
            #tracker.pop(detection['id'])
            # tracker[0] = {}
            history = {}
            print('I am popping')

        else:
            print("i am getting a strike")
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
    
if __name__ == '__main__':
    app.run(port=5000)
    
    
