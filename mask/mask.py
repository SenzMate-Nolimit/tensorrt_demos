import numpy as np
import matplotlib.pyplot as plt
import cv2
import json

variable_nano_file_path = "/home/jetson-nl1/Downloads/tensorrt_demos/variable_nano.json"
with open(variable_nano_file_path, 'r') as file:
    json_data = file.read()
parsed_data = json.loads(json_data)
mask_coordinates = parsed_data['mask_coordinates']


def plot_line(frame):

    img_name = "points/sample.png"
    img = cv2.imread(img_name)
    h, w = img.shape[:2]
    height, width = frame.shape[:2]

    edge_coordinates = [[int((a / w) * width), int((b / h) * height)] for a, b in mask_coordinates]
    mask = np.ones((height,width))
    mask.fill(-1)
    roi_corners = np.array([edge_coordinates], dtype=np.int32)
    cv2.fillPoly(mask, roi_corners, (1))

    return mask

