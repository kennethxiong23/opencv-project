import cv2 as cv
import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-i', "--image", required=True, help = "Image path")

args = vars(ap.parse_args())
image = cv.imread(args["image"])
cv.imshow("original", image)

mask = np.zeros(image.shape[:2], dtype = "uint8")
(cX, cY) = (image.shape[1] // 2, image.shape[0] // 2)
cv.rectangle(mask, (cX - 75, cY - 75), (cX + 75, cY + 75), 255, -1)

cv.imshow("Mask", mask)

masked = cv.bitwise_and(image, image, mask = mask)
cv.imshow("masked", masked)
cv.waitKey(0)
