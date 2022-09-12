from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import argparse
import cv2 as cv

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "path to image file")
ap.add_argument("-s", "--size", required = False, help= "size of largest color bin", default = 5000)
ap.add_argument("-b", "--bins", required = False, help = "number of bins per color channged"
    , default = 8)

args = vars(ap.parse_args())

image = cv.imread(args["image"])
size = float(args["size"])
bins = int(args["bins"])

hist = cv. calcHist([image], [0,1,2], None, [bins, bins, bins], [0,256,0,256,0,256])

hist = cv.calcHist([image], [0,1,2], None, [8,8,8], [0,256,0,256,0,256])
print("3d hisotriagram with shape %s and values %s" %(hist.shape, hist.flatten().shape[0]))

fig = plt.figure()
ax = fig.add_subplot(111, projection = "3d")
ratio = size / np.max(hist)

for (x, plane) in enumerate(hist):
    for (y, row) in enumerate(plane):
        for (z, col) in enumerate(row):
            if hist[x][y][z] > 0.0:
                siz = ratio *hist [x][y][z]
                rgb = (z/(bins - 1), y / (bins - 1), x / (bins - 1))
                ax.scatter(x,y,z, s = siz, facecolors = rgb)
plt.show()
