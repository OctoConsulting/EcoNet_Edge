from bh_runner.decode_stream import *
from bh_runner.klv_validation import *
import argparse
import sys
import cv2
from tqdm import tqdm
from yolo_inference.yolo_inference_engine import YoloInferenceEngine

# take in path to a image
def main(source):
    # convert to np array
    frame_num = 0
    sampling_rate = 6
    
    conf_thresh=0.25
    weights = 'yolov5s.pt'
    inf_eng = YoloInferenceEngine(weights, conf_thresh=conf_thresh)

    for df in tqdm(decode_stream(source)):
        results = None
        if frame_num % sampling_rate == 0:
            results = inf_eng.do_inference(df)

            display_result(results, df)
            # l = list_results(results,df)
            # print(l)    

            # TODO l should look like this 

            # l = {
            #     'detections': [
            #         {
            #             'x1' : 1,
            #             'x2' : 1,
            #             'y1' : 1,
            #             'y2' : 1,
            #             'lable' : 'person', 
            #             'image' : bytearray encoded as base64
            #         },
            #         {
            #             'x1' : 1,
            #             'x2' : 1,
            #             'y1' : 1,
            #             'y2' : 1,
            #             'lable' : 'person',
            #             'image' : bytearray encoded as base64
            #         },
            #     ]
            # }

            # send l through a websocket to toto pre prossessing

        frame_num += 1


def list_results(results, img):
    image = make_image(results, img)
    r = []
    for detect in results:
        e = {}
        e['label'] = detect.label
        e['x1'] = detect.x1
        e['x1'] = detect.x2
        e['y1'] = detect.y1
        e['y2'] = detect.y2
        e['image'] = image

        r.append(e)
    
    l = {}
    l['detections'] = r

    return l

# this should draw a box around the object in the image and then turn that image into a byte array
# return a byte array
def make_image(results, img):
    if results:
        for detect in results:

            # draw bounding boxes
            cv2.rectangle(img, (int(detect.x1), int(detect.y1)), (int(detect.x2), int(detect.y2)), (255, 0, 0), 1)

    return img

def display_result(results, img):
    if results:
        for detect in results:

            # draw bounding boxes
            cv2.rectangle(img, (int(detect.x1), int(detect.y1)), (int(detect.x2), int(detect.y2)), (255, 0, 0), 1)
            # cv2.putText(img, str(detect.label), (int(detect.x1), int(detect.y1) + 5), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            #             fontScale=0.5, color=(0, 0, 255), thickness=1)
    
    cv2.namedWindow("Display", cv2.WINDOW_NORMAL)
    cv2.imshow("Display", img)
    #delay= int(1000 / 500)
    cv2.waitKey(1)



if __name__ == '__main__':
    main(sys.argv[1])