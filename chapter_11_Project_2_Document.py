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
    # 1. Converting to greyscale 
    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    
    # 2. Apply Blur
    imgBlur = cv.GaussianBlur(imgGray,(5,5),1)
    
    # Find Edges
    imgCanny = cv.Canny(imgBlur, 200,200)
    
    # Dilation and Erosion
    kernel = np.ones((5,5))
    imgDialation = cv.dilate(imgCanny, kernel , iterations = 2)
    imgThreshold = cv.erode(imgDialation, kernel, iterations = 1)
    
    return imgThreshold


while True:
    success, img = WebCam.read()
    
    # Resize width and height of img
    cv.resize(img, (widthImg, heightImg))
    # Show result
    cv.imshow("WEBCAM", img)
    
    # Add Delay and Key to Break loop
    if cv.waitKey(33) & 0xFF==ord("q"):
        break
    
