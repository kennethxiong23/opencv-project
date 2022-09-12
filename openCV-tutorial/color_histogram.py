from matplotlib import pyplot as plt
import numpy as np
import cv2 as cv
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "path to file")
args = vars(ap.parse_args())

image = cv.imread(args["image"])

cv.imshow("original", image)

chans = cv.split(image)
colors = ("b", "g", "r")
plt.figure()
plt.title("Flattened Color Historiogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")

for (chan, color) in zip(chans,colors):
    hist = cv.calcHist([chan], [0], None, [256], [0,256])
    plt.plot(hist, color = color)
    plt.xlim([0,256])
plt.show()
fig = plt.figure()

ax = fig.add_subplot(131)
hist = cv.calcHist([chans[1], chans[0]], [0,1], None, [32,32], [0,256,0,256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title("2d color Historiogram of g and b")
plt.colorbar(p)

ax = fig.add_subplot(132)
hist = cv.calcHist([chans[1], chans[2]], [0,1], None, [32,32], [0,256,0,256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title("2d color Historiogram of g and r")
plt.colorbar(p)

ax = fig.add_subplot(133)
hist = cv.calcHist([chans[2], chans[0]], [0,1], None, [32,32], [0,256,0,256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title("2d color Historiogram of r and b")
plt.colorbar(p)

fig.show()
print("2d Historiogram shape: %s, with %s values"%(hist.shape, hist.flatten().shape))
cv.waitKey(0)
