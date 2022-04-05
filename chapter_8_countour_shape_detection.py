# Imports
from inspect import stack
import cv2 as cv
from matplotlib.pyplot import contour
import numpy as np

from my_functions_open_cv.stacking import stackImages

# Read files
path = "./resources/images/shapes.png"
img = cv.imread(path)


# Apply effect
imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
imgBlur = cv.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv.Canny(imgBlur, 50,50)


# Copy original image to prepare for contour detection
imgContour = img.copy()

# Blank image
imgBlank = np.zeros_like(img)


# Function for finding contour

def getContours(img):
    contours,hierarchy = cv.findContours(img,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
    for cnt in contours:
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



#print Contours
getContours(imgCanny)



# Stack images together
imgStack = stackImages(1,([img,imgGray,imgBlur],
                            [imgCanny,imgContour,imgBlank]))

# Display Image

cv.imshow("IMAGES", imgStack)
cv.waitKey(0)