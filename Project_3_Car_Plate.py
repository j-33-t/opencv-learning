 # Imports
import cv2 as cv
from cv2 import putText
import numpy as np

from my_functions_open_cv.stacking import stackImages

widthImg, heightImg = 540, 640

# ################    
#  Using Webcam  #
# ################
frameWidth = 640
frameHeight = 480
WebCam = cv.VideoCapture(0)
WebCam.set(3,frameWidth)
WebCam.set(4,frameHeight)
WebCam.set(10,150)

# Loading Cascade
CarPlateCascade = cv.CascadeClassifier("./resources/cascade/haarcascade_russian_plate_number.xml")

# Min area variable
minArea = 500

# Color 
color = (255,0,255)

while True:
    success, img = WebCam.read()
    
    # Exit screen
    
    
    # Convert image to GrayScale
    imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    
    # Identify Plate
    numberPlates = CarPlateCascade.detectMultiScale(imgGray,1.1,4)

    # Create Bounding Boxes around faces

    for (x,y,w,h) in numberPlates:
        area = w*h
        if area > minArea:
            cv.rectangle(img,(x,y),(x+w,y+h),color,2)
            cv.putText(img,"Number Plate",(x,y-5),cv.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
        imgRoi = img[y:y+h,x:x+w]
        cv.imshow("region of interest", imgRoi)
        
    # Show result
    cv.imshow("WEBCAM", img)
    
    count = 0    
    # save scan
    if cv.waitKey(1) & 0xFF == ord('s'):
        cv.imwrite("Resources/plate_numbers_saved/NoPlate_"+str(count)+".jpg",imgRoi)
        cv.rectangle(img,(0,200),(640,300),(0,255,0),cv.FILLED)
        cv.putText(img,"Scan Saved",(150,265),cv.FONT_HERSHEY_DUPLEX,
                    2,(0,0,255),2)
        cv.imshow("Result",img)
        cv.waitKey(10)
        count +=1

    
    

