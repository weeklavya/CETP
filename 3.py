 

import os
import pytesseract
from PIL import Image
import tempfile
import subprocess
import cv2
import time
cam = cv2.VideoCapture(0)
 


ret = True
while ret:
    ret, img = cam.read()
    img = cv2.imread('thres.png',cv2.IMREAD_COLOR) #Open the image from which charectors has to be recognized
    #img = cv2.resize(img, (620,480) ) #resize the image if required
    cv2.imshow('img',img)
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert to grey to reduce detials
    gray = cv2.bilateralFilter(gray, 11, 17, 17) #Blur to reduce noise

    original = pytesseract.image_to_string(gray, config='eng' )
    test = (pytesseract.image_to_data(gray, lang=None, config='-l eng --oem 3 --psm 12') ) #get confidence level if required
    print(test)

    print (original)    
    if 0xFF & cv2.waitKey(5) == 27:
        break

cv2.destroyAllWindows()
 
 


