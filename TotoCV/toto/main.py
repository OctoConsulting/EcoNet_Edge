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
    sampling_rate = 1

    for df in tqdm(decode_stream(source)):
        if frame_num % sampling_rate == 0:
            img = df

            conf_thresh=0.25
            weights = 'yolov5s.pt'
            
            inf_eng = YoloInferenceEngine(weights, conf_thresh=conf_thresh)
            
            results = inf_eng.do_inference(img)

    display_result(results, img)

    l = list_results(results)

    return l

def display_result(results, img):
    for detect in results:

        # draw bounding boxes
        cv2.rectangle(img, (int(detect.x1), int(detect.y1)), (int(detect.x2), int(detect.y2)), (255, 0, 0), 3)
        cv2.putText(img, str(detect.label), (int(detect.x1), int(detect.y1) + 5), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=0.5, color=(0, 0, 255), thickness=1)
    
    cv2.namedWindow("Display", cv2.WINDOW_NORMAL)
    cv2.imshow("Display", img)
    cv2.waitKey(1)

def list_results(results):
    r = []
    for detect in results:
        e = {}
        e['label'] = detect.label
        e['x1'] = detect.x1
        e['x1'] = detect.x2
        e['y1'] = detect.y1
        e['y2'] = detect.y2

        r.append(e)

    return r


if __name__ == '__main__':
    print(main(sys.argv[1]))