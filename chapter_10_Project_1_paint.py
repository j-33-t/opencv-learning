# imports
import cv2 as cv
import numpy as np

## Trackbars don't work on mac :(

# Define color parameters - [need to adjust color according to camera sensitivity]

myColors = [[5,107,0,19,255,255]]

myColorValues = [[51,153,255]] # BGR

myPoints = [] ## [x , y , colorId ]

# Function for finding color
def findColor(img, myColors, myColorValues):
    imgHSV = cv.cvtColor(img,cv.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    for color in myColors:  
        lower = np.array(myColors[0][0:3])
        upper = np.array(myColors[0][3:6])
        mask = cv.inRange(imgHSV,lower,upper)
        # cv.imshow(str(color[0]),mask)
        x,y = getContoursPaint(mask)
        cv.circle(imgResult, (x,y),10,myColorValues[count],cv.FILLED)
        if x != 0 and y != 0:
            newPoints.append([x,y,count])
        count += 1
    return newPoints


def getContoursPaint(img):
    contours,hierarchy = cv.findContours(img,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv.contourArea(cnt)
        if area > 500:
        # print(area)
            # cv.drawContours(imgResult,cnt,-1,(255,0,0),3)
            peri = cv.arcLength(cnt,True)
            # print(peri)
            approx = cv.approxPolyDP(cnt,0.02*peri,True)
            x,y,w,h = cv.boundingRect(approx)
        
    return x+w//2,y

def drawOnCanvas(myPoints,myColorValues):
    for point in myPoints:
                cv.circle(imgResult, (point[0],point[1]),10,myColorValues[point[2]],cv.FILLED)

        
    

WebCam = cv.VideoCapture(0)
WebCam.set(3,640) #width has id no. 3
WebCam.set(4,480) #height has id no.4

while True:
    success, img = WebCam.read()
    img = cv.flip(img,1)
    imgResult = img.copy()
    newPoints = findColor(img, myColors, myColorValues)
    if len(newPoints) != 0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints) != 0:
        drawOnCanvas(myPoints,myColorValues)
    # Show result
    cv.imshow("WEBCAM", imgResult)
    
    # Add Delay and Key to Break loop
    if cv.waitKey(33) & 0xFF==ord("q"):
        break




