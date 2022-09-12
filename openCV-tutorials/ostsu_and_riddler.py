import numpy as np
import mahotas
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

T = mahotas.thresholding.otsu(blurred)
print("otsu threshold %s" %T)

thresh = image.copy()
thresh[thresh>T] = 255
thresh[thresh<T] = 0

thresh = cv.bitwise_not(thresh)

cv.imshow("otsu", thresh)

T = mahotas.thresholding.rc(blurred)
print("Ridder threshold %s" %T)

thresh = image.copy()
thresh[thresh>T] = 255
thresh[thresh<T] = 0

thresh = cv.bitwise_not(thresh)

cv.imshow("Ridder", thresh)

cv.waitKey(0)
