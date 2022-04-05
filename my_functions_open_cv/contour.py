# Imports
from inspect import stack
import cv2 as cv
from matplotlib.pyplot import contour
import numpy as np

# Contour Function for shapes

def getContours(img):
    contours,hierarchy = cv.findContours(img,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
    for cnt in contours:
        imgContour = img.copy()
        area = cv.contourArea(cnt)
        # print(area)
        cv.drawContours(imgContour,cnt,-1,(255,0,0),3)
        peri = cv.arcLength(cnt,True)
        # print(peri)
        approx = cv.approxPolyDP(cnt,0.02*peri,True)
        print(len(approx))
        objCor = len(approx)
        x,y,w,h = cv.boundingRect(approx)
        
        if objCor == 3:
            objectType  = "Triangle"
        elif objCor == 4:
            aspRatio = w/float(h)
            if aspRatio > 0.95 and aspRatio < 1.05:
                objectType = "Square"
            else:
                objectType = "Rectangle"
        elif objCor > 4:
            objectType = "Circle"
        else:
            objectType = "None"
            
        cv.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
        cv.putText(imgContour, objectType, 
                   (x+(w//2)-10, 
                   y+(h//2)),
                   cv.FONT_HERSHEY_COMPLEX,
                   0.7,(0,0,0),2)
        
        
    return




