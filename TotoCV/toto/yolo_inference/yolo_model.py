import os
import torch


def yolo_model(weights_path, classes=None, max_dets=100, conf_thresh=0.25, iou_thresh=0.5):
    """
    Create a yolo model instance for doing inference
    @param weights_path: path to saved yolo5 weights file (.pt file)
    @type weights_path: str
    @param classes: list of classes to include, if None includes all classes the model predicts
    @type classes: list
    @param max_dets: max detections allowed per image
    @type max_dets: int
    @param conf_thresh: confidence filtering threshold
    @type conf_thresh: float
    @param iou_thresh: NMS iou threshold
    @type iou_thresh: float
    @return: yolo5 pytorch model
    @rtype: AutoShape pytorch model
    """
    if os.path.splitext(weights_path)[1].lower() == '.pt':
        model = torch.hub.load('ultralytics/yolov5', 'custom', weights_path, force_reload=False)
    else:
        model = torch.hub.load('ultralytics/yolov5', weights_path)
    model.conf = conf_thresh
    model.classes = classes
    model.max_det = max_dets
    model.iou = iou_thresh
    model.eval()
    return model
