# Import necessary packages
import cv2
import collections
import numpy as np
from .tracker import *

# Initialize Tracker
tracker = EuclideanDistTracker()

# Defining input size
input_size = 320


# Detection confidence threshold
confThreshold = 0.2
nmsThreshold = 0.2


# Middle cross line position
middle_line_position = 225
up_line_position = middle_line_position - 15
down_line_position = middle_line_position + 15


# Store Coco Names in a list
classesFile = "stream/coco.names"
classNames = open(classesFile).read().strip().split('\n')


# class index for our required detection classes
required_class_index = [2, 3, 5, 7]
detected_classNames = []


# Model Files
modelConfiguration = 'stream/yolov3-320.cfg'
modelWeigheights = 'stream/yolov3-320.weights'


# configure the network model
net = cv2.dnn.readNetFromDarknet(modelConfiguration, modelWeigheights)


# # Configure the network backend
# net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
# net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)


# Define random colour for each class
np.random.seed(42)
colors = np.random.randint(0, 255, size=(len(classNames), 3), dtype='uint8')


# Function for finding the center of a rectangle
def find_center(x, y, w, h):
    x1 = int(w/2)
    y1 = int(h/2)
    cx = x+x1
    cy = y+y1
    return cx, cy


# List for store vehicle count information
temp_up_list = []
temp_down_list = []
up_list = [0, 0, 0, 0]
down_list = [0, 0, 0, 0]


# Function for count vehicle
def count_vehicle(box_id):
    x, y, w, h, id, index = box_id


    # Find the center of the rectangle for detection
    center = find_center(x, y, w, h)
    ix, iy = center


    # Find the current position of the vehicle
    if (iy > up_line_position) and (iy < middle_line_position):
        if id not in temp_up_list:
            temp_up_list.append(id)

    elif iy < down_line_position and iy > middle_line_position:
        if id not in temp_down_list:
            temp_down_list.append(id)

    elif iy < up_line_position:
        if id in temp_down_list:
            temp_down_list.remove(id)
            up_list[index] = up_list[index]+1

    elif iy > down_line_position:
        if id in temp_up_list:
            temp_up_list.remove(id)
            down_list[index] = down_list[index] + 1


# Function for finding the detected objects from the network output
def postProcess(outputs, img):
    global detected_classNames
    height, width = img.shape[:2]
    boxes = []
    classIds = []
    confidence_scores = []
    for output in outputs:
        for det in output:
            scores = det[5:]
            classId = np.argmax(scores)
            confidence = scores[classId]
            if classId in required_class_index:
                if confidence > confThreshold:
                    w, h = int(det[2]*width), int(det[3]*height)
                    x, y = int((det[0]*width)-w/2), int((det[1]*height)-h/2)
                    boxes.append([x, y, w, h])
                    classIds.append(classId)
                    confidence_scores.append(float(confidence))

    # Apply Non-Max Suppression
    indices = cv2.dnn.NMSBoxes(
        boxes, confidence_scores, confThreshold, nmsThreshold)
    
    

    for i in indices:
        name = classNames[classIds[i]]
        detected_classNames.append(name)


def from_static_image(img):
    global detected_classNames
    blob = cv2.dnn.blobFromImage(
        img, 1 / 255, (input_size, input_size), [0, 0, 0], 1, crop=False)

    net.setInput(blob)
    layersNames = net.getLayerNames()
    outputNames = [(layersNames[i - 1]) for i in net.getUnconnectedOutLayers()]
    # Feed data to the network
    outputs = net.forward(outputNames)

    # Find the objects from the network output
    postProcess(outputs, img)

    # count the frequency of detected classes
    frequency = collections.Counter(detected_classNames)
    total = 0
    for i in frequency:
        total += frequency[i]
    detected_classNames=[]
    return total