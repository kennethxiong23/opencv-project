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

canny = cv.Canny(image, 105, 250)
cv.imshow("canny", canny)
cv.waitKey(0)

(cnts, _) = cv.findContours(canny.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
print("i count %s coins" %len(cnts))

coins = image.copy()
cv.drawContours(coins, cnts, -1, (0,255,0), 2)
cv.imshow("coints", coins)
cv.waitKey(0)
