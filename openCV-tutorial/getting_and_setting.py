import argparse
import cv2 as cv


parser = argparse.ArgumentParser()
parser.add_argument("--i", "--image", required = True, help = "path to image")
args = vars(parser.parse_args())

image = cv.imread(args["i"])
cv.imshow("original", image)

b, g, r = image[0,0]
print("pixel at 0,0, red: %s, blue: %s, green %s" %(r,g,b))

corner = image[0:100, 0:100]
cv.imshow("corner", corner)

image[0:100, 0:100] = (0,0,255)
b, g, r = image[0,0]
cv.imshow("updated", image)
print("pixel at 0,0, red: %s, blue: %s, green %s" %(r,g,b))
cv.waitKey(0)
