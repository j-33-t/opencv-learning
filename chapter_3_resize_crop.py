# """ 
#                     CONCEPT ALERT !!
#     Concept about x and y axis in computer graphics [OPENCV]
    
#     X axis is the same in opencv as regular math concept
    
#     But positive y axis is towards the south in opencv
    
#     Point of origin is on the top left corner.
# """

# Imports
import cv2 as cv

# Read image

img = cv.imread("./resources/images/cr7.jpeg")

# Find Size of Image
print(f"Original Image Dimension: {img.shape}") # output = width, height, color channel [for rgb = 3]

# Resize Image [Small]
imgResizeS = cv.resize(img, (300,200)) # width,height
print(f"Resize Image Dimension [S]: {imgResizeS.shape}")


# Resize Image [Large]
imgResizeL = cv.resize(img, (1000,700)) # width,height
print(f"Resize Image Dimension [L]: {imgResizeL.shape}")


# Cropping Image

#  " Image itself is just a matrix or an array of pixels
#   Therefore we can deal with it like an array or matrix "

imgCropped = img[0:413, 200:500]  # Here we have height first and width 

# Display Images
cv.imshow("Original Image", img) # Display image (window name, image)
# cv.imshow("Resized Image Small", imgResizeS)
# cv.imshow("Resized Image Large", imgResizeL)
cv.imshow("Cropped Image", imgCropped)  
cv.waitKey(0) # Adding delay [0 = infinite delay, 1000 = 1 second]
