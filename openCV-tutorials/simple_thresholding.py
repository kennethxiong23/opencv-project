import cv2 as cv
import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "image path")
args = vars(ap.parse_args())

image = cv.imread(args["image"])

image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
blurred = cv.GaussianBlur(image, (5,5), 0)
cv.imshow("image", image)

(T, thresh) = cv.threshold(blurred, 155, 255, cv.THRESH_BINARY)
cv.imshow("Threshoild binary", thresh)

(T, threshInv) = cv.threshold(blurred, 155, 255, cv.THRESH_BINARY_INV)
cv.imshow("THresthold binary inverse", threshInv)

cv.imshow("Coins", cv.bitwise_and(image, image, mask = threshInv))

cv.waitKey(0)
