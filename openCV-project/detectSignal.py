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

    #display video/webcam feed
    while True:
        ret, frame = vid.read()
        frame = cv.flip(frame, 0)

        cv.imshow("frame", frame)
        if cv.waitKey(1) == ord('q'):
            break
    cv.destroyAllWindows()



main()
