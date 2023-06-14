from decode_stream import *
from klv_validation import *
from geoprojection import *
from tqdm import tqdm
import argparse
import sys
import cv2

# sys.path.insert(0, "/c/Users/SakethRajesh/Documents/EcoNet/cv_intern_2023/yolo_inference")
# sys.path.append('../yolo_inference')
from ..yolo_inference.yolo_inference_engine import YoloInferenceEngine


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', required=True, default=None)
    parser.add_argument('--weights', type=str, default='yolov5s.pt')
    parser.add_argument('--sampling-rate', required=False, default=1, type=int, help="run inference on every x frame")
    parser.add_argument('--rgb-inference', required=False, action="store_true", help="Run inference on rgb")
    parser.add_argument('--conf-thresh', required=False, default=0.25)
    parser.add_argument('--view-results', required=False, action="store_true")


    args = parser.parse_args()

    bh_runner(args.source, args.weights, args.sampling_rate, args.rgb_inference, args.conf_thresh, args.view_results)


def bh_runner(source, weights, sampling_rate=1, rgb_inference=True, conf_thresh=0.25, view_results=True):

    """
    load the model via our inference class
    """
    inf_eng = YoloInferenceEngine(weights, conf_thresh=conf_thresh)

    frame_num = 0

    for df in tqdm(decode_stream(source)):
        if frame_num % sampling_rate == 0:
            # check that the klv meta data is valid
            # valid_klv = validate_klv(df.meta)
            img = df
            # img = df.thermal.copy()
            # if rgb_inference:
            #     img = df.rgb.copy()
            results = inf_eng.do_inference(img)
            detections = []
            for detect in results:
                # draw bounding boxes
                if view_results:
                    cv2.rectangle(img, (int(detect.x1), int(detect.y1)), (int(detect.x2), int(detect.y2)), (255, 0, 0), 3)
                    cv2.putText(img, str(detect.label), (int(detect.x1), int(detect.y1) + 5), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                fontScale=0.5, color=(0, 0, 255), thickness=1)
                # if valid_klv:
                #     detc = [(detect.x1 + detect.x2) / 2, (detect.y1 + detect.y2) / 2]
                #     easting, northing, lon, lat = r = project_to_world_with_klv(df.meta, detc)
                #     detection = {
                #         "center": [easting, northing],
                #         "lon": lon,
                #         "lat": lat,
                #         "label": detect.label,
                #         "xyxy": [detect.x1, detect.y1, detect.x2, detect.y2]}
                #     detections.append(detection)
            if view_results:
                cv2.namedWindow("Display", cv2.WINDOW_NORMAL)
                cv2.imshow("Display", img)
                cv2.waitKey(1)
        frame_num += 1


if __name__ == '__main__':
    try:
        bh_runner(source="rtsp://olabs:olabs123@172.26.24.72:554/h264Preview_01_sub", weights="yolov5s.pt", sampling_rate=1, rgb_inference=True, conf_thresh=0.25, view_results=True)
    except KeyboardInterrupt:
        sys.exit(0)
