import cv2 as cv
import numpy as np

canvas = np.zeros((300,300,3), dtype = "uint8")
green = (0,255,0)
cv.line(canvas, (0,0), (300,300), green)

red = (0,0,255)
cv.line(canvas,(0,300), (300,0),red, 3)
cv.imshow("canvas", canvas)
cv.waitKey(0)

cv.rectangle(canvas, (10,10), (60,60), green)
cv.imshow("canvas", canvas)
cv.waitKey(0)

cv.rectangle(canvas, (50, 200), (200,225), red, -1)
cv.imshow("canvas", canvas)
cv.waitKey(0)

canvas = np.zeros((300,300,3), dtype = "uint8")
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
white = (255, 255, 255)

for r in range(0, 175, 25):
    cv. circle(canvas, (centerX, centerY), r, white)
cv.imshow("canvas", canvas)
cv.waitKey(0)

for i in range(0,25):
    radius = np.random.randint(5, high=200)
    color = np.random.randint(0, high=300, size=(3,)).tolist()
    pt = np.random.randint(0, high=canvas.shape[1], size=(2,))
    cv.circle(canvas, tuple(pt), radius, color, -1)
cv.imshow('canvas', canvas)
cv.waitKey(0)
