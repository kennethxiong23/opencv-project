import numpy as np
import cv2 as cv
import argparse
from matplotlib import pyplot as plt

def plot_histogram(image, title, mask = None):
    chans = cv.split(image)
    colors = ('b', "g", 'r')
    plt.figure()
    plt.title(title)
    plt.xlabel("Bins")
    plt.ylabel("# of pixels")

    for (chan, color) in zip(chans, colors):
        hist = cv.calcHist([chan], [0], mask, [256], [0,256])
        plt.plot(hist, color=color)
        plt.xlim([0,256])

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "image path")
args = vars(ap.parse_args())

image = cv.imread(args["image"])
cv.imshow("original", image)
plot_histogram(image, "histogram for original image")

mask = np.zeros(image.shape[:2], dtype = "uint8")
cv.rectangle(mask, (15,15), (130,100), 255, -1)
cv.imshow("mask", mask)

masked = cv.bitwise_and(image,image, mask= mask)
cv.imshow("applied mask image", masked)

plot_histogram(image, "histogram for masked image", mask = mask)
plt.show()
