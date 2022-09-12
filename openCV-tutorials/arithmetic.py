import numpy as np
import argparse
import cv2 as cv

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help = "path to image")

args = vars(ap.parse_args())

image = cv.imread(args["image"])
cv.imshow("original", image)

M = np.ones(image.shape, dtype="uint8") * 100
added = cv.add(image, M)

cv.imshow("added", added)

M = np.ones(image.shape, dtype = "uint8") * 50

subtracted = cv.subtract(image, M)
cv.imshow("subtracted", subtracted)

cv.waitKey(0)
