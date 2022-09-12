import numpy as np
import cv2 as cv
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help ="image path")

args = vars(ap.parse_args())

image = cv.imread(args["image"])
image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow("original", image)

blurred = cv.GaussianBlur(image, (5,5),0)

cv.imshow("IMAGE", image)

canny = cv.Canny(image, 30, 150)
cv.imshow("canny", canny)
cv.waitKey(0)
