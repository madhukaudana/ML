import time
from pymata4 import pymata4
import os
import numpy as np
import cv2
import argparse
import sys
import os.path
# import ML_

count = 0
trigpin = 11
ecopin = 12

board = pymata4.Pymata4()

def the_callback(data):
    global count
    print("Distance: ", data[2])
    if data [2] < 100:
        os.system("python ML_.py")
        # exec(open("/Users/madhukaw/Documents/Image_Recognition/ML_.py").read())


board.set_pin_mode_sonar(trigpin,ecopin,the_callback)

while True:
    try:
        time.sleep(0.1)
        board.sonar_read(trigpin)

    except Exception:
        board.shutdown()