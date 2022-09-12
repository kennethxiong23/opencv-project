import numpy as np
import cv2 as cv
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "image path")
args = vars(ap.parse_args())

image = cv.imread(args["image"])
cv.imshow("orignal", image)

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow("grey", gray)

hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
cv.imshow("hsv", hsv)

lab = cv.cvtColor(image, cv.COLOR_BGR2LAB)
cv.imshow("L*a*b", lab)

cv.waitKey(0)
