
# Imports 
import cv2 as cv
import numpy as np

# Define Shape of Image
img = np.zeros((512,512,3),np.uint8) # Blank Canvas

# Find dimension of image
print(img.shape)


# # Color Everything on Canvas Hence [:]
# img[:] = 255,0,0

# # Colro Specific Part
# img[200:300, 100:300] = 255,0,0

# Draw Line

cv.line(img,(0,0),(300,300),(0,255,0),3) # arguments = (img, (starting point), (width, height), (color), thickness)
# cv.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3) # arguments = (img, (starting point), (img.shape[width], img.shape[height]), (color), thickness)


# Draw Rectangle/Square

cv.rectangle(img, (0,0),(300,300),(0,0,255),3)

# Fill Rectangle/Square
cv.rectangle(img, (0,0),(100,100),(0,255,0),cv.FILLED)
# - experimentation with dimensions
# cv.rectangle(img, (10,0),(100,100),(0,255,0),cv.FILLED)
# cv.rectangle(img, (0,10),(100,100),(0,255,0),cv.FILLED)
# cv.rectangle(img, (10,10),(100,100),(0,255,0),cv.FILLED)
# cv.rectangle(img, (75,10),(100,100),(0,255,0),cv.FILLED)

# Draw Circle
cv.circle(img,(400,400), 30,(255,255,0),5)

# Write Text
cv.putText(img, "OPEN CV", (320,100), cv.FONT_HERSHEY_TRIPLEX,1.1,(0,150,0),1)

# Display Image
cv.imshow("Canvas", img)
cv.waitKey(0)