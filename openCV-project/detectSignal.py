"""
    Description: This program detects what orientation the signal cone is in for
                for the 2022-23 FTC game Power Play using open cv.
    Name: Kenneth Xiong
    Date: Sep 12 22
"""
import argparse
import numpy as np
import cv2 as cv

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", required = False, default = 0,
                help = "Path to video, defaults to webcam")
args = vars(ap.parse_args())

def main():
    vid = cv.VideoCapture(args["video"])
    #hsv values for thresholding
    low_H = 110
    low_S = 28
    low_V = 0
    high_H = 146
    high_S = 255
    high_V= 255
    # display video/webcam feed
    while True:
        ret, frame = vid.read()
        if args["video"] != 0:
            frame = cv.flip(frame, 0)
        #image preprocessing
        frame = cv.GaussianBlur(frame, (19,19), 0)
        hsvFrame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        threshold = cv.inRange(hsvFrame, (low_H, low_S, low_V), (high_H, high_S, high_V))
        (cnts, _) = cv.findContours(threshold.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        # for (i,c) in enumerate(cnts):
        #     (x,y,w,h) = cv.boundingRect(c)
        #     cone = frame[y:y+h, x:x+w]
        #     cv.imshow("countor", cone)
        #     cv.waitKey(0)
        image = frame.copy()
        cv.drawContours(image, cnts, -1, (0,255,0), 2)
        cv.imshow("image", image)
        cv.imshow("frame", frame)
        cv.imshow("hsv threshold", threshold)
        cv.imshow("hsv ", hsvFrame)
        #click q to stop
        if cv.waitKey(1) == ord('q'):
            break





main()
