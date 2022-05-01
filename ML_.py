# Usage:
# python yolo.py --video=<path to video file>
# python yolo.py --image=<path to image file>

import pickle
import pymongo
import pandas as pdq
import numpy as np
import cv2
import argparse
import sys
import numpy as np
import os.path
import time
from flask import Flask

product_details = {}
# create set

oldWeight=100
reduce_weight = 80
new_weight = 120

#totalPrice=1

itemSet = set()
compList = []
details =[]
# pickle_off = open ("datafile.txt", "rb")
# compList= pickle.load(pickle_off)
# print(compList)

# connecting mongodb database,
client = pymongo.MongoClient("localhost:27017")
database = client["ProductDetails"]
mycol = database["SDGP"]

records=mycol.find()
dbList = list(records)


# Initialize the parameters
confThreshold = 0.5  # Confidence threshold
nmsThreshold = 0.4  # Non-maximum suppression threshold
parser = argparse.ArgumentParser(description='Object Detection using YOLO in OPENCV')
parser.add_argument('--image', help='Path to image file.')
parser.add_argument('--video', help='Path to video file.')
args = parser.parse_args()

# Load names of classes from coco

classes = open('../YOLOv3/coco.names').read().strip().split('\n')

net = cv2.dnn.readNetFromDarknet("../YOLOv3/yolov3.cfg", "../YOLOv3/yolov3.weights")
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)


# Get the names of the output layers
def getOutputsNames(net):
    # Get the names of all the layers in the network
    layersNames = net.getLayerNames()
    # Get the names of the output layers, i.e. the layers with unconnected outputs
    return [layersNames[i - 1] for i in net.getUnconnectedOutLayers()]


# Draw the predicted bounding box
def drawPred(classId, conf, left, top, right, bottom):
    count = 0
    # Draw a bounding box.
    cv2.rectangle(frame, (left, top), (right, bottom), (255, 178, 50), 3)

    label = '%.2f' % conf

    # Get the label for the class name and its confidence
    if classes:
        assert (classId < len(classes))
        label = '%s:%s' % (classes[classId], label)

    # Display the label at the top of the bounding box
    labelSize, baseLine = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
    top = max(top, labelSize[1])
    cv2.rectangle(frame, (left, top - round(1.5 * labelSize[1])), (left + round(1.5 * labelSize[0]), top + baseLine),
                  (255, 255, 255), cv2.FILLED)
    cv2.putText(frame, label, (left, top), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 0), 1)


    # adding detected item into a set
    itemSet.add(classes[classId])
    return itemSet


def calculation(itemSet):
    count = 0
    for item in itemSet:
            # if new_weight < oldWeight:
            #     for x in range(0, len(compList)):
                    # if compList[x] == item:
                    #     #calculating deducted price
                    #     for element in dbList:
                    #         if element['productName'] == item:
                    #             name = element['productName']
                    #             price = element['productPrice']
                    #             weight = element['productWeight(g)']
                    #             reducedPrice=((weight-new_weight)*(price/weight))/100
                    #             #totalPrice-=reducedPrice
                    #
                    #             product_details = {"name": name, "productPrice": price, "productQuantity": 1,
                    #                                "imgPath": "images/watermelon.jpg", "totalPrice": 350.00}
                    #             app = Flask(__name__)
                    #
                    #             @app.route("/productDetails")
                    #             def members():
                    #                 return product_details
                    #
                    #             if __name__ == "__main__":
                    #                 app.run(debug=True)
                    #
                    #     # print(x)
                    #     del compList[x]
                    #     print(compList)

            if new_weight > oldWeight:
                if item not in compList:
                    compList.append(item)
                    count = count + 1
                    with open('datafile.txt', 'wb') as fh:
                        pickle.dump(compList, fh)
                    for element in dbList:
                        if element['productName'] == item:
                            name=element['productName']
                            price = element['productPrice']
                            weight = element['productWeight(g)']
                            finalPrice = ((new_weight - oldWeight) * (price / weight)) / 100
                            #totalPrice += finalPrice
                            print("Price: ",round(finalPrice, 2))

                            for i in range(len(compList)):
                                file_details = [
                                    {
                                        "name": "banana",
                                        "price": round(finalPrice, 2),
                                        "image": "images/banana.jpg",
                                        "quantity": 1,
                                        "totalPrice": totalPrice
                                    }
                                ]
                                # # serializing  json
                                # json_object = json.dumps(file_details, indent=4)
                                #
                                # # writing to details.json
                                # with open("details.json", "w") as json_file:
                                #     json_file.write(json_object)
                                # # loading json file
                            with open("details.json", 'r+') as file:
                        # First we load existing data into a dict.

                        file_data = json.load(file)
                        # Join new_data with file_data inside emp_details
                        for i in range(len(compList)):
                            new_data = {

                                "name": compList[i],
                                "price": round(finalPrice, 2),
                                "image": "images/hiruni.jpg",
                                "quantity": 1,
                                "totalPrice": totalPrice

                            }
                        file_data.append(new_data)
                        # Sets file's current position at offset.
                        file.seek(0)
                        # convert back to json.
                        json.dump(file_data, file, indent=4)

                if count >= 1:
                    # sys.exit()
                    print(compList)


# product_details = {"name": "watermelon", "productPrice": 350, "productQuantity": 1,
#                        "imgPath": "images/watermelon.jpg", "totalPrice": 350.00}
# product_details={"a","b"}
# app = Flask(__name__)
#
# @app.route("/productDetails")
# def members():
#     return product_details
#
# if __name__ == "__main__":
#     app.run(debug=True)

    # print(classId)
    #  print(label)
#abc
#bla
# Remove the bounding boxes with low confidence using non-maxima suppression
def postprocess(frame, outp):
    frameHeight = frame.shape[0]
    frameWidth = frame.shape[1]

    # Scan through all the bounding boxes output from the network and keep only the
    # ones with high confidence scores. Assign the box's class label as the class with the highest score.
    classIds = []
    confidences = []
    boxes = []
    for out in outp:
        for detection in out:
            scores = detection[5:]
            classId = np.argmax(scores)
            confidence = scores[classId]
            if confidence > confThreshold:
                center_x = int(detection[0] * frameWidth)
                center_y = int(detection[1] * frameHeight)
                width = int(detection[2] * frameWidth)
                height = int(detection[3] * frameHeight)
                left = int(center_x - width / 2)
                top = int(center_y - height / 2)
                classIds.append(classId)
                confidences.append(float(confidence))
                boxes.append([left, top, width, height])

    # Perform non maximum suppression to eliminate redundant overlapping boxes with
    # lower confidences.
    indices = cv2.dnn.NMSBoxes(boxes, confidences, confThreshold, nmsThreshold)
    for i in indices:
        i = i
        box = boxes[i]
        left = box[0]
        top = box[1]
        width = box[2]
        height = box[3]
        drawPred(classIds[i], confidences[i], left, top, left + width, top + height)


        calculation(itemSet)
        # app = Flask(__name__)
        #
        # @app.route("/productDetails")
        # def members():
        #     return product_details
        #
        # if __name__ == "__main__":
        #     app.run(debug=True)


# outputFile = "YOLOv3_output.avi"
if (args.image):
    # Open the image file
    if not os.path.isfile(args.image):
        print("Input image file ", args.image, " doesn't exist")
        sys.exit(1)
    # cap = cv2.VideoCapture(args.image)
    # outputFile = args.image[:-4] + '_YOLOv3_output.jpg'
else:
    # Open the video file
    cap = cv2.VideoCapture(0)

# Get the video writer initialized to save the output video
# if (not args.image):
#     vid_writer = cv2.VideoWriter(outputFile, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 30,
#                                  (round(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))

while cv2.waitKey(1) < 0:

    hasFrame, frame = cap.read()

    # Stop if end of video
    if not hasFrame:
        # print("File with YOLOv3 output is here :  ", outputFile)
        cv2.waitKey(5000)
        cap.release()
        break

    # Create a 4D blob from a frame.
    blob = cv2.dnn.blobFromImage(frame, 1 / 255, (416, 416), [0, 0, 0], 1, crop=False)

    # Sets the input to the network
    net.setInput(blob)

    # Runs the forward pass to get output of the output layers
    outp = net.forward(getOutputsNames(net))

    # Remove the bounding boxes with low confidence
    postprocess(frame, outp)

    # Write the frame with the detection boxes
    # if (args.image):
    #     cv2.imwrite(outputFile, frame.astype(np.uint8))
    # else:
    #     vid_writer.write(frame.astype(np.uint8))

    cv2.imshow('Image', frame)
