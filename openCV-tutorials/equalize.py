import cv2 as cv
import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "image path")
args = vars(ap.parse_args())

image = cv.imread(args["image"])

image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

eq = cv.equalizeHist(image)

cv.imshow("histogram equalization", np.hstack([image, eq]))
cv.waitKey(0)
