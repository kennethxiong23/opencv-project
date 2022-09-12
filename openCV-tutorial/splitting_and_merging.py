import numpy as np
import cv2 as cv
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "image path")
args = vars(ap.parse_args())

image = cv.imread(args["image"])
cv.imshow("orignal", image)
(B, G, R) = cv.split(image)

cv.imshow("Red", R)
cv.imshow("Green", G)
cv.imshow("Blue", B)
cv.waitKey(0)

zeros = np.zeros(image.shape[:2], dtype = "uint8")
cv.imshow("red", cv.merge([zeros, zeros, R]))
cv.imshow("Green", cv.merge([zeros, G, zeros]))
cv.imshow("Blue", cv.merge([B, zeros, zeros]))
cv.waitKey(0)

merged = cv.merge([B,G,R])
cv.imshow("merged", merged)
cv.waitKey(0)
cv.waitKey(0)
cv.destroyAllWindows()
