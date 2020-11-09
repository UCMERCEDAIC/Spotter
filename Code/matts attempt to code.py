
import sys
from random import randint
import cv2 
import numpy
import os
import time
import imutils

# Constants for finding range of skin color in YCrCb
min_YCrCb = numpy.array([0,133,77],numpy.uint8)
max_YCrCb = numpy.array([255,173,127],numpy.uint8)

hog = cv2.HOGDescriptor() 
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

for file in os.listdir("squats"):
    x = file
    # Opening image 
    src = cv2.imread("squats/"+ x)
    
    # will show the image in a window 
    #cv2.imshow('image', src) 
    #k = cv2.waitKey(0) & 0xFF
    

   # videoFrame = src

    # Process the video frames
   # keyPressed = 97 # -1 indicates no key pressed

    #while(keyPressed < 0): # any key pressed has a value >= 0

        # Grab video frame, decode it and return next video frame
   # sourceImage = videoFrame

    # Convert image to YCrCb
    #imageYCrCb = cv2.cvtColor(sourceImage,cv2.COLOR_BGR2YCR_CB)

    # Find region with skin tone in YCrCb image
   # skinRegion = cv2.inRange(imageYCrCb,min_YCrCb,max_YCrCb)

    # Do contour detection on skin region
   # contours, hierarchy = cv2.findContours(skinRegion, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw the contour on the source image
    #for i, c in enumerate(contours):
        #area = cv2.contourArea(c)
       # if area > 100:
           # cv2.drawContours(sourceImage, contours, i, (0, 255, 0), 3)


    #status = cv2.imwrite("Images_processed/"+ x,sourceImage)

    # Display the source image
    #cv2.imshow('Camera Output',sourceImage)

    # Check for user input to close program
    #keyPressed = 92 # wait 1 milisecond in each iteration of while loop

    # Close window and camera after exiting the while loop
   
   
   # Reading the Image 
    image = src
    
    # Resizing the Image 
    image = imutils.resize(image, 
                        width=min(400, image.shape[1])) 
    
    # Detecting all the regions in the  
    # Image that has a pedestrians inside it 
    (regions, _) = hog.detectMultiScale(image,  
                                        winStride=(1, 1), 
                                        padding=(526, 526), 
                                        scale=1.05) 
    
    # Drawing the regions in the Image 
    for (x, y, w, h) in regions: 
        cv2.rectangle(image, (x, y),  
                    (x + w, y + h),  
                    (0, 0, 255), 2) 
    
    # Showing the output Image 
    cv2.imshow("Image", image) 
    cv2.waitKey(0) 
    
    cv2.destroyAllWindows() 
   

   



