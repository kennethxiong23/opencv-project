import numpy as np
import cv2 as cv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--image", required=True, help = "image path")

args = vars(parser.parse_args())

image = cv.imread(args["image"])
cv.imshow("original", image)

cropped = image[30:120, 240: 335]

cv.imshow("trex face", cropped)

cv.waitKey(0)
