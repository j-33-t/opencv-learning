import cv2 as cv
import numpy as np

# Loading Cascade
faceCascade = cv.CascadeClassifier("./resources/cascade/haarcascade_frontalface_default.xml")

# Read Image
img = cv.imread("./resources/faces/Mbappe-Haaland-Messi-Ronaldo.jpeg")

# Apply grayscale
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Detect Faces
faces = faceCascade.detectMultiScale(imgGray,1.1,4)

# Create Bounding Boxes around faces

for (x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    

# Show image
cv.imshow("Result", img)
cv.waitKey(0)