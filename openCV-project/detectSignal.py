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
ap.add_argument("-v", "--video", required = False, default = None,
                help = "Path to video")
ap.add_argument("-i", "--image", required = False, default = None,
                help = "Path to image")
ap.add_argument("-c", "--camera", required = False, default = None,
                help = "integer representing the camera(if only one device, 0)")
args = vars(ap.parse_args())

def main():
    if args["camera"] != None:
        vid = cv.VideoCapture(int(args["camera"]))
    elif args["video"] != None:
        vid = cv.VideoCapture(args["video"])
    elif args["image"] != None:
        vid = cv.imread(args["image"])
    #hsv values for thresholding
    low_H = 125
    low_S = 55
    low_V = 124
    high_H = 150
    high_S = 255
    high_V= 255
    # display video/webcam feed
    while True:
        #need to flip video
        if args["image"] != None:
            frame = vid
            ret, frame = vid.read()
            frame = cv.flip(frame, 0)
        else:
            ret, frame = vid.read()
            if args["video"] != None:
                frame = cv.flip(frame, 0)


        image = frame.copy()
        #image preprocessing
        frame = cv.GaussianBlur(frame, (33,33), 0)
        hsvFrame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        threshold = cv.inRange(hsvFrame, (low_H, low_S, low_V), (high_H, high_S, high_V))
        #morphology?
        kernel1 = cv.getStructuringElement(cv.MORPH_ELLIPSE, (23,23))
        kernel2 = np.ones((15,15), np.uint8)
        eroded = cv.erode(threshold, kernel1, iterations = 1)
        open = cv.dilate(threshold, kernel2, iterations = 1)
        # dilate = cv.dilate(threshold, (20,20), iterations = 1)
        # kernel = np.ones((5,5),np.uint8)
        # open = cv.erode(threshold, kernal, iterations = 1)
        # open = cv.morphologyEx(threshold, cv.MORPH_CLOSE, (10,10))
        # open = cv.GaussianBlur(open, (17,17), 0)
        # erod =
        # closing = cv.morphologyEx(open, cv.MORPH_CLOSE, (20,20))
        # eroded = cv.erode(closing, (25,25), iterations = 1)
        # open = cv.morphologyEx(eroded, cv.MORPH_OPEN, (7,7))
        (cnts, _) = cv.findContours(open.copy(),cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
        if len(cnts) > 0:
            # c = max(cnt, key=cv.)
            for c in cnts:
                (x,y,w,h) = cv.boundingRect(c)
            # mask = np.zeros(image.shape[:2], dtype='uint8')
                cv.rectangle(image, (x, y), (x+w, y+h), (0,255,0), 3)
        # cv.rectangle(mask, (x, y), (x+w, y+h), (0,255,0), 2)
        # cone = cv.bitwise_and(image, image, mask=mask)

        # cv.drawContours(image,[box],0,(0,0,255),2)
        # for (i,c) in enumerate(cnts):
        #     (x,y,w,h) = cv.boundingRect(c)
        #     rectangle = cv.rectangle(image, (x, y), (x+w, y+h), (0,255,0), 2)
        # cv.drawContours(image, cnts, -1, (0,255,0), 2)
        # cv.imshow("open", open)
        # cv.imshow("Cone", cone)
        cv.imshow("Image", image)
        # cv.imshow("frame", frame)
        cv.imshow("mask", open)
        # cv.imshow("hsv ", hsvFrame)
        #click q to stop
        if cv.waitKey(1) == ord('q'):
            break

main()
