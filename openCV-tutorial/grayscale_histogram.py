from matplotlib import pyplot as plt
import numpy as np
import cv2 as cv
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "image path")
args = vars(ap.parse_args())

image = cv.imread(args["image"])
image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow("orignal", image)
hist = cv.calcHist([image], [0], None, [256], [0, 256])

plt.figure()
plt.title("grayscale Historiogram")
plt.xlabel("bins")
plt.ylabel("# of pixels")
plt.plot(hist)
plt.xlim([0,256])
plt.show()
cv.waitKey(0)
