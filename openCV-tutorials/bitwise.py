import cv2 as cv
import numpy as np

rectangle = np.zeros((300,300), dtype= "uint8")
cv.rectangle(rectangle, (25,25), (275,275), 255, -1)
cv.imshow("rectangle", rectangle)

circle = np.zeros((300,300), dtype="uint8")
red = (255,0,0)
cv.circle(circle, (150,150), 150, 255, -1)
cv.imshow('circle', circle)

bitwiseAnd = cv.bitwise_and(rectangle, circle)
cv.imshow("AND", bitwiseAnd)

bitwiseOr = cv.bitwise_or(rectangle,circle)
cv.imshow("or", bitwiseOr)

bitwiseXor = cv.bitwise_xor(rectangle, circle)
cv.imshow("xor", bitwiseXor)

bitwiseNot = cv.bitwise_not(rectangle, circle)
cv.imshow("not", bitwiseNot)
cv.waitKey(0)
