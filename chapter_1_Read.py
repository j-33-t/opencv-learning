# Imports
import cv2 as cv

##########################
# Steps to Reading Image #
##########################

img = cv.imread("./resources/images/cr7.jpeg")
cv.imshow("Cristiano Ronaldo", img) # Display image (window name, image)
cv.waitKey(0) # Adding delay [0 = infinite delay, 1000 = 1 second]


#########################
# Steps tp read a Video #
#########################

cap = cv.VideoCapture("./resources/videos/cr7.mp4")

# """ 
# Since video is a collection of images we will need
# a while loop to display all the frame continously
# """

while True:
    success, img = cap.read()
    
    # Show result
    cv.imshow("Video", img)
    
    # Add Delay and Key to Break loop
    if cv.waitKey(35) & 0xFF==ord("q"):
        break
    
# ################    
# # Using Webcam #
# ################

WebCam = cv.VideoCapture(0)
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
    
