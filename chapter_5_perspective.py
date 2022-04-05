import cv2 as cv
import numpy as np

# Read Image
img = cv.imread("./resources/images/cards.jpeg")

width,height = 250,350

pts1 = np.float32([[148,106],[347,36],[295,356],[512,274]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv.getPerspectiveTransform(pts1,pts2)

imgOutput = cv.warpPerspective(img,matrix,(width,height))

# Show image
cv.imshow("Image", img)
cv.imshow("Output", imgOutput)
cv.waitKey(0)
