import argparse
import cv2 as cv


parser = argparse.ArgumentParser()
parser.add_argument("--i", "--image", required = True, help = "path to image")
args = vars(parser.parse_args())

image = cv.imread(args["i"])
print("width: %s pixels" %image.shape[1])
print("height: %s pixels" %image.shape[0])

cv.imshow("Image", image)
cv.waitKey(0)

cv.imwrite("newimage.jpg", image)
