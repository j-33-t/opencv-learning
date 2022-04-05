import cv2 as cv
import numpy as np

img = cv.imread("./resources/images/cr7.jpeg")

# 1 - Converting into greyscale
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) #Greyscale
cv.imshow("Grey Image", imgGray)
cv.waitKey(0)

# # 2 - Adding Blue to Image

imgBlur = cv.GaussianBlur(imgGray, (7,7), 0) # arugments in GaussianBlue are as follows - image, ksize - has to be odd number, sigmaX
cv.imshow("Blur Image", imgBlur)
cv.waitKey(0)

# # 3 - Edge Detection [Detector type = CANNY]

imgCanny = cv.Canny(img, 150,200) # change thresholds to change number of edges
cv.imshow("Edge Detector (CANNY) ", imgCanny)
cv.waitKey(0)

# 4 - Edge Detection [Detector type = CANNY] + Joining Edges usig Dilation [Making Edges thicker]

kernel = np.ones((5,5), np.uint8)
imgDilation = cv.dilate(imgCanny, kernel,iterations = 1)
cv.imshow("canny + dilation", imgDilation)
cv.waitKey(0)

# # 5 - Edge Detection [Detector type = CANNY] + Erosion [Making Edges Thinner]
imgEroded = cv.erode(imgDilation,kernel,iterations = 1)
cv.imshow("Erosion", imgEroded)
cv.waitKey(0)