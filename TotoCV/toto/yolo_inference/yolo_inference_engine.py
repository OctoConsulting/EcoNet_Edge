from .detect import Detect
from scripts.AppLogger import configure_logger
from .yolo_model import yolo_model

class YoloInferenceEngine:
    def __init__(self, weights_path, classes=None, inf_size=None, max_dets=100, conf_thresh=0.25, iou_thresh=0.5,
                 label_map=None):
        """
        Loads model from torch hub and sets model properties
        @param weights_path: path to saved pytorch model pt file
        @type weights_path: str
        @param classes: list of classes to include, if None includes all classes the model predicts
        @type classes: list
        @param inf_size: resamples image to this size maintaining aspect ratio, if None don't resize. Represents new
        image width
        @type inf_size: int
        @param max_dets: max detections allowed per image
        @type max_dets: int
        @param conf_thresh: confidence filtering threshold
        @type conf_thresh: float
        @param iou_thresh: NMS iou threshold
        @type iou_thresh: float
        """
        self.log = configure_logger("bhRunner")
        self.model = yolo_model(weights_path, classes, max_dets, conf_thresh, iou_thresh)
        self.log.info('Model instantiated from: ' + weights_path)
        if classes is None:
            self.log.info('Model instantiated without classes')
        else:
            self.log.info('Model instantiated with classes: ' + str(classes))
        self.log.info('Model instantiated with confidence threshold: ' + str(conf_thresh))
        self.inf_size = inf_size
        if label_map is not None:
            self.label_map = self._reverse_label_map(label_map)
            self.log.info('Label map being used: ' + label_map)
        else:
            self.label_map = None

    @staticmethod
    def _reverse_label_map(label_map):
        """
        Takes a label map where keys are new labels and value are list of old values and reverses it, so keys are old
        labels and values are new labels
        @param label_map: dict where keys are new labels and value are list of old values
        @type label_map: dict
        @return: dict where keys are old labels and values are new labels
        @rtype: dict
        """
        reversed_map = {}
        for new_label, old_label_list in label_map.items():
            for old_label in old_label_list:
                reversed_map[old_label] = new_label
        return reversed_map

    def do_inference(self, img):
        """
        Does inference on an image then returns detections
        @param img: image to do inference on
        @type img: np array
        @return: list of detections from img
        @rtype: list of Detect
        """
        if self.inf_size is not None:
            pred = self.model([img], size=self.inf_size)
        else:
            pred = self.model([img])
        pred = pred.xyxy[0].cpu().numpy()
        detect_list = []
        for det in pred:  # detections per image
            if self.label_map is None:
                if int(det[5]) == 0:
                    detect = Detect(int(det[0]), int(det[1]), int(det[2]), int(det[3]), str('person'), det[4])
                    detect_list.append(detect)
            else:
                if int(det[5]) in self.label_map:
                    label = self.label_map[int(det[5])]
                    detect = Detect(int(det[0]), int(det[1]), int(det[2]), int(det[3]), label, det[4])
                    detect_list.append(detect)
        return detect_list
