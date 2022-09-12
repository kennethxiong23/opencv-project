import numpy as np
import argparse
import imutils
import cv2 as cv

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--image", required=True, help="Path to Image")
args = vars(parser.parse_args())

image = cv.imread(args["image"])
cv.imshow("first one", image)

M = np.float32([[1,0,25], [0, 1, 50]])
shifted = cv.warpAffine(image, M, (50,20t))
cv.imshow("shifted down and right", shifted)

M = np.float32([[1,0,-5], [0, 1, -90]])
shifted = cv.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv.imshow("shifted up and left", shifted)

image = imutils.translate(shifted, 0, 100)
cv.imshow("shifted down", image)

cv.waitKey(0)
