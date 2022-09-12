import numpy as np
import cv2 as cv
import imutils
import argparse

ap =  argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "path to file")
args = vars(ap.parse_args())

image = cv.imread(args["image"])
cv.imshow("original", image)

(h,w) = image.shape[:2]
center = (w // 2, h // 2)

M = cv.getRotationMatrix2D(center, 45, 1.0)
rotated = cv.warpAffine(image, M, (w,h))
cv.imshow("rorate by 45 degrees", rotated)

M = cv.getRotationMatrix2D(center, -90, 1.0)
rotated = cv.warpAffine(image, M, (w,h))
cv.imshow("rorate by -90 degrees", rotated)

rotated = imutils.rotate(image, 180)
cv.imshow("rotated by 180", rotated)

cv.waitKey(0)
