# Imports
import cv2 as cv
import numpy as np

# #########################  
# # Using Webcam Function #
# #########################


def Cam(WebCam = cv.VideoCapture(0)):
    WebCam.set(3,640) #width has id no. 3
    WebCam.set(4,480) #height has id no.4
    WebCam.set(10,100) #brightness has id no.10


    while True:
        success, img = WebCam.read()
        
        # Show result
        cv.imshow("WEBCAM", img)
        
        # Add Delay and Key to Break loop
        if cv.waitKey(33) & 0xFF==ord("q"):
            break
    
    return

