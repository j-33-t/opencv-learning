# Imports
import cv2 as cv
import numpy as np

widthImg, heightImg = 640,480

# ################    
# # Using Webcam #
# ################

WebCam = cv.VideoCapture(0)
WebCam.set(3,widthImg) #width has id no. 3
WebCam.set(4,heightImg) #height has id no.4
WebCam.set(10,100) #brightness has id no.10


def preProcessing(img):
    imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    imgBlur = cv.GaussianBlur(imgGray,(5,5),1)
    imgCanny = cv.Canny(imgBlur,200,200)
    kernel = np.ones((5,5))
    imgDial = cv.dilate(imgCanny,kernel,iterations=2)
    imgThres = cv.erode(imgDial,kernel,iterations=1)
    return imgThres





def getContours(img):
    biggest = np.array([])
    maxArea = 0
    contours,hierarchy = cv.findContours(img,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv.contourArea(cnt)
        if area > 5000:
            cv.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri = cv.arcLength(cnt,True)
            approx = cv.approxPolyDP(cnt,0.02*peri,True)
            if area > maxArea and len(approx) == 4:
                biggest = approx
                maxArea = area        
#     cv.drawContours(imgContour, biggest, -1, (255, 0, 0), 20)
    return biggest


# def getWarp(img, biggest):
    
#     pass

while True:
    success, img = WebCam.read()
    
    # Resize width and height of img
    cv.resize(img, (widthImg, heightImg))
    
    # Copy img 
    imgContour = img.copy()
    
    # Adding imgThreshold
    imgThres = preProcessing(img)
    
    # # Adding contour to imgThreshold
    getContours(imgThres)
    # getWarp(img,biggest)
    
    # Flip image
    imgThres = cv.flip(imgThres,1)
    
    # Show results
    cv.imshow("Result", imgContour)
    
    # Add Delay and Key to Break loop
    if cv.waitKey(33) & 0xFF==ord("q"):
        break
    
