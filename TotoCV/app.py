from flask import Flask, request, jsonify
from flask_sock import Sock
import toto
import os
import subprocess
import json

from tqdm import tqdm
from toto.yolo_inference.yolo_inference_engine import YoloInferenceEngine
from toto.bh_runner.decode_stream import *
from toto.bh_runner.klv_validation import *
import cv2
import base64

# this is localhost:8000

app = Flask(__name__)
sock = Sock(app)

###########################################################
# this should manage comunication with the main porgram
###########################################################
@app.route('/toto/main', methods=['POST'])
def point():

    return

@sock.route('/toto/<drone_ip>', methods=['GET'])
def stream(ws,drone_ip=None):

    if not drone_ip:
        return "error"
    

    try: 

        live = 'rtsp://' + drone_ip + '/live'
        frame_num = 0
        sampling_rate = 6
        conf_thresh=0.25
        weights = 'yolov5s.pt'

        inf_eng = YoloInferenceEngine(weights, conf_thresh=conf_thresh)

        while True:
            for df in tqdm(decode_stream(live)):
                results = None
                if frame_num % sampling_rate == 0:
                    results = inf_eng.do_inference(df)


                    # send l through a websocket to toto pre prossessing
                    # load as json first
                    l = list_results(results, df)
                    ws.send(json.dumps(l))

            frame_num += 1

    except KeyboardInterrupt:
            pass

    stream.stop_stream()
    stream.close()


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