import cv2
import numpy as np
import PIL # necessary for pytesseract
import pytesseract # wrapper for tesseract-ocr

height = 400 # height of image
width  = 600 # width of image

image = cv2.resize(cv2.imread("crop.jpg"), (width, height)) # loading and resizing image
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
info = [x for x in info.splitlines() if not x.isspace() and x] # noise reduction in list

index = 0 # index will store the index value of DOB field
for field in enumerate(info): # field is a tuple of index number and corresponding string
    if "DOB" in field[1]:
        index = field[0]
        break
else:
    print("Please provide a clean and better cropped image!")
    exit()

try:
    name = info[index-1] # name extraction
    print("Name:", name)
except IndexError:
    print("Cannot find name. Please provide a clean and better cropped image!")

try:
    dob = info[index] # date of birth extraction
    dob = dob[dob.index("DOB"):]
    print(dob)
except IndexError:
    print("Cannot find DOB. Please provide a clean and better cropped image!")

try:
    if "female" in info[index+1].casefold(): # gender extraction
        gender = "Female"
    else:
        gender = "Male"
    print("Gender:", gender)
except IndexError:
    print("Cannot find gender. Please provide a clean and better cropped image!")

try:
    uid = info[index+2] # Extracting UID
    print(uid)
except IndexError:
    print("Cannot find UID. Please provide a clean and better cropped image!")

cv2.destroyAllWindows()

cv2.imshow()