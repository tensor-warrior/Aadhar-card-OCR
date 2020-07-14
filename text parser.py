import cv2
import numpy as np
import PIL # necessary for pytesseract
import pytesseract # wrapper for tesseract-ocr

height = 400 # height of image
width  = 600 # width of image

image = cv2.resize(cv2.imread("crop.jpg"), (width, height)) # loading and resizing image

lookUpTable = np.empty((1, 256), np.uint8) # applying gamma correction
gamma = 0.4 # hard-coded for this value
for i in range(256):
    lookUpTable = np.clip(pow(i/255.0, gamma)*255.0, 0, 255)
    
image = cv2.LUT(image, lookUpTable)

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # converting image into grayscale

kernel = np.array([5,5], np.uint8)
erosion = cv2.erode(image_gray, kernel, iterations=1) # applying erosion

ret, thresh = cv2.threshold(erosion, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV) # applying OTSU threshold

contours, heirarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # obtaining all the contours

for c in contours: # removal of unnecessary elements
    rect = cv2.boundingRect(c)
    x, y, w, h = rect
    area = w*h

    if area not in range(1000, 100000): # contours having area in this range will not be removed
        continue

    image[y:y+h, x:x+w] = (255,255,255) # replacing unnecessary elements with white blobs

cv2.imshow("Filtered image", image)
cv2.waitKey(0)

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

info = pytesseract.image_to_string(image_gray, lang="eng") # parsing text in processed aadhar blob
info = [x for x in info.splitlines() if not x.isspace() and x] # getting rid of whitespaces

for i in info:
   print(i) 

cv2.destroyAllWindows()

cv2.imshow()
