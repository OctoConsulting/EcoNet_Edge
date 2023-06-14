from decode_stream import *
from klv_validation import *
from geoprojection import *
from tqdm import tqdm
import argparse
import sys
import cv2

################
# realtive path import stuff
################
sys.path.append('../yolo_inference')
from yolo_inference.yolo_inference_engine import YoloInferenceEngine

def main(df):

    conf_thresh=0.25
    weights = 'yolov5s.pt'
    
    inf_eng = YoloInferenceEngine(weights, conf_thresh=conf_thresh)
        
    img = df
    results = inf_eng.do_inference(img)
    detections = []


if __name__ == '__main__':
    main(sys.argv[1])