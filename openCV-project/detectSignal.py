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

def createMask(img, thresholdLB, thresholdUB):
    """
    Purpose: Applies preprocessing(blur/morph ops) and creates a mask for
    contour drawing.
    Parameters: image frame, hsv threshold(np.array()) lower bound and upper bound
    to apply.
    Return Val: a black and white image mask
    """
    #image preprocessing
    blurredFrame = cv.GaussianBlur(img, (33,33), 0)
    #thresholding
    hsvFrame = cv.cvtColor(blurredFrame, cv.COLOR_BGR2HSV)
    threshold = cv.inRange(hsvFrame, thresholdLB, thresholdUB)
    #morphology ops
    kernel1 = cv.getStructuringElement(cv.MORPH_ELLIPSE, (23,23))
    kernel2 = np.ones((15,15), np.uint8)
    #eliplical erode to get rid of some of the noise
    erodedFrame = cv.erode(threshold, kernel1, iterations = 1)
    openFrame = cv.dilate(erodedFrame, kernel2, iterations = 1)

    return openFrame

def findLargestContour(mask1, mask2, mask3):
    """
    Purpose: finds the mask that has the largest contour. This should mean
            that the color the mask represents is the one being shown.
    Parameters: 3 different masks
    Return Val: the mask that has the largest contour
    """
    #detect contours
    (cnts1, _) = cv.findContours(mask1.copy(),cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
    (cnts2, _) = cv.findContours(mask2.copy(),cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
    (cnts3, _) = cv.findContours(mask3.copy(),cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
    cnts = [cnts1, cnts2, cnts3]
    #find the max contour
    maxC = np.array([])
    maxMask = None
    for c in cnts:
        if len(c) != 0 :
            if maxC.size == 0:
                maxC = max(c, key=cv.contourArea)
                maxMask = c
            else:
                if cv.contourArea(max(c, key=cv.contourArea)) > cv.contourArea(maxC):
                    maxC = max(c, key=cv.contourArea)
                    maxMask = c

    #find the largest mask
    if maxC in cnts1:
        return mask1, maxC
    if maxC in cnts2:
        return mask2, maxC
    else:
        return mask3, maxC

def main():
    #check which input was used
    if args["camera"] != None:
        vid = cv.VideoCapture(int(args["camera"]))
    elif args["video"] != None:
        vid = cv.VideoCapture(args["video"])
    elif args["image"] != None:
        vid = cv.imread(args["image"])

    #hsv values for thresholding
    cyanHSV_LB = np.array([75,50,0])
    cyanHSV_UB = np.array([110,255,255])

    yellowHSV_LB = np.array([10,50,0])
    yellowHSV_UB = np.array([30,255,255])

    magentaHSV_LB = np.array([150,50,0])
    magentaHSV_UB = np.array([175,255,255])

    # display video/webcam feed
    while True:
        #check if video needs to be flipped
        if args["image"] != None:
            frame = vid
            ret, frame = vid.read()
            frame = cv.flip(frame, 0)
        else:
            ret, frame = vid.read()
            if args["video"] != None:
                frame = cv.flip(frame, 0)

        #get masks for each option/color
        cyanMask = createMask(frame, cyanHSV_LB, cyanHSV_UB)
        yellowMask = createMask(frame, yellowHSV_LB, yellowHSV_UB)
        magentaMask = createMask(frame, magentaHSV_LB, magentaHSV_UB)
        solutionMask = findLargestContour(cyanMask, yellowMask, magentaMask)
        if solutionMask[1].size > 0:
            (x,y,w,h) = cv.boundingRect(solutionMask[1])
            cv.rectangle(frame, (x, y), (x+w,y+h), (0,255,0), 2)

        if np.array_equal(solutionMask[0], cyanMask):
            print("pos 3")
        elif np.array_equal(solutionMask[0], yellowMask):
            print("pos 1")
        else:
            print("pos2")

        cv.imshow("Image", frame)
        if cv.waitKey(1) == ord('q'):
            break

main()
