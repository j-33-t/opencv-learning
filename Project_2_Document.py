# Imports
import cv2 as cv
import numpy as np

from my_functions_open_cv.stacking import stackImages

widthImg, heightImg = 540, 640

# ################    
#  Using Webcam  #
# ################

WebCam = cv.VideoCapture(0)
WebCam.set(10,150)

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
        if area>5000:
            peri = cv.arcLength(cnt,True)
            approx = cv.approxPolyDP(cnt,0.02*peri,True)
            if area >maxArea and len(approx) == 4:
                biggest = approx
                maxArea = area
    cv.drawContours(imgContour, biggest, -1, (255, 0, 0), 20)
    return biggest

def reorder (myPoints):
    myPoints = myPoints.reshape((4,2))
    myPointsNew = np.zeros((4,1,2),np.int32)
    add = myPoints.sum(1)

    myPointsNew[0] = myPoints[np.argmin(add)]
    myPointsNew[3] = myPoints[np.argmax(add)]
    diff = np.diff(myPoints,axis=1)
    myPointsNew[1]= myPoints[np.argmin(diff)]
    myPointsNew[2] = myPoints[np.argmax(diff)]

    return myPointsNew

def getWarp(img,biggest):
    biggest = reorder(biggest)
    pts1 = np.float32(biggest)
    pts2 = np.float32([[0, 0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])
    matrix = cv.getPerspectiveTransform(pts1, pts2)
    imgOutput = cv.warpPerspective(img, matrix, (widthImg, heightImg))

    imgCropped = imgOutput[20:imgOutput.shape[0]-20,20:imgOutput.shape[1]-20]
    imgCropped = cv.resize(imgCropped,(widthImg,heightImg))

    return imgCropped

    
# While Loop to display the Webcam Document Reading program

while True:
    success, img = WebCam.read()
    
    # Resize width and height of img
    img = cv.resize(img,(widthImg,heightImg))
    
    # Copy img
    imgContour = img.copy()

    # Pre-processing Image
    imgThres = preProcessing(img)
    
    # Adding contour to imgThreshold
    biggest = getContours(imgThres)
    
    # Avoid Error when biggest size is not found
    if biggest.size !=0:
        # Warping Image
        imgWarped=getWarp(img,biggest)

        imageArray = ([imgContour, imgWarped])
        cv.imshow("ImageWarped", imgWarped)
    else:

        imageArray = ([imgContour, img])

    # Stacking Images
    stackedImages = stackImages(0.6,imageArray)
    
    # Show results
    cv.imshow("WorkFlow", stackedImages)

    # Add Delay and Key to Break loop
    if cv.waitKey(1) & 0xFF == ord('q'):
        break