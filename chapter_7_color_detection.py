import cv2 as cv
import numpy as np

from my_functions_open_cv.stacking import stackImages

# Create trackbars
def empty(a):
    pass

# 56,80,61,255,0,255
cv.namedWindow("TrackBars")
cv.resizeWindow("TrackBars",640,240) 
cv.createTrackbar("Hue Min","TrackBars",56,179,empty)
cv.createTrackbar("Hue Max","TrackBars",80,179,empty)
cv.createTrackbar("Sat Min","TrackBars",61,255,empty)
cv.createTrackbar("Sat Max","TrackBars",255,255,empty)
cv.createTrackbar("Val Min","TrackBars",0,255,empty)
cv.createTrackbar("Val Max","TrackBars",255,255,empty)

# Run everything in a loop

while True:
# Read Image
    img = cv.imread("./resources/images/cards.jpeg")

# Task :  detect RED Color in the image

    # Step 1. Convert to HSV 
    imgHSV = cv.cvtColor(img,cv.COLOR_BGR2HSV)

    # Step 2. Define color values & ranges in which we want our color to be
    # 2.1 Adjust hue, saturation and value limits
    h_min = cv.getTrackbarPos("Hue Min","TrackBars")
    h_max = cv.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv.getTrackbarPos("Val Max", "TrackBars")
    print(h_min,h_max,s_min,s_max,v_min,v_max)

    # Creating Mask
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv.inRange(imgHSV,lower,upper)
    
    imgResult = cv.bitwise_and(img,img,mask = mask)

    # Show image
    
    # cv.imshow("orginal", img)
    # cv.imshow("HSV", imgHSV)
    # cv.imshow("Mask", mask)
    # cv.imshow("Result", imgResult)
    
    imgStack = stackImages(0.6, ([img,imgHSV],[mask,imgResult]))
    cv.imshow("Stacked Images", imgStack)
    cv.waitKey(1)
    

    