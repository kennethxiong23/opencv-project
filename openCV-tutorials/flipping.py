import argparse
import cv2 as cv

ap =  argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "path to file")
args = vars(ap.parse_args())

image = cv.imread(args["image"])
cv.imshow("original", image)

flipped = cv.flip(image, 1)
cv.imshow("flipped horizontaly", image)

cv.waitKey(0)
