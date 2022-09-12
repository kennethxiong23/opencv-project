import cv2 as cv
import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "image path")
args = vars(ap.parse_args())

image = cv.imread(args["image"])
cv.imshow("original", image)

#averaging
blurred = np.hstack([
    cv.blur(image, (3,3)),
    cv.blur(image, (5,5)),
    cv.blur(image, (7,7))
])

cv.imshow("average", blurred)

#gaussin blurr
blurred = np.hstack([
    cv.GaussianBlur(image, (3,3), 0),
    cv.GaussianBlur(image, (5,5), 0),
    cv.GaussianBlur(image, (7,7), 0)

])
cv.imshow("guassian", blurred)

#mediaan blur
blurred = np.hstack([
    cv.medianBlur(image, 3),
    cv.medianBlur(image, 5),
    cv.medianBlur(image, 7)
])

cv.imshow("median", blurred)

#bilateral blurr
blurred = np.hstack([
    cv.bilateralFilter(image, 5, 21, 21),
    cv.bilateralFilter(image, 7, 31, 31),
    cv.bilateralFilter(image, 9, 100,100)
])
cv.imshow("bilateral", blurred)

cv.waitKey(0)
