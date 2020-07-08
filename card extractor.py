import cv2
import numpy as np
import utils

height = 400 # height of image
width  = 600 # width of image

img = cv2.resize(cv2.imread("Sample Images\gulshan aadhar.jpg"), (width, height)) # Loading and resizing image
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Converting image to grayscale

gaussian_blur = cv2.GaussianBlur(img_gray, (5, 5), 1) # Blurring with Gaussian blur

edges = cv2.Canny(gaussian_blur, 50, 150) # Detecting with Canny edge detector

kernel = np.ones((5, 5)) # Kernel dimension is set to 5*5
dilation = cv2.dilate(edges, kernel, iterations=2) # Applying dilation
thresh = cv2.erode(dilation, kernel, iterations=1)  # Applying erosion

all_contours = img.copy() # Creating a copy of image to draw all contours
biggest_contour = img.copy() # Creating a copy of image to draw the biggest contours

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # Obtaining all contours
cv2.drawContours(all_contours, contours, -1, (0, 255, 0), 2) # Drawing all detected contours
cv2.imshow("All contours", all_contours)
cv2.waitKey(0)

biggest, maxArea = utils.biggestContour(contours) # Obtaining the end points of biggest contour
biggest = utils.reorder(biggest)
cv2.drawContours(biggest_contour, biggest, -1, (0, 255, 0), 5) # Drawing end points of the biggest contour

biggest_contour = utils.drawRectangle(biggest_contour, biggest, 2) # Drawing the boundary of card
cv2.imshow("Biggest contour", biggest_contour)
cv2.waitKey(0)

pts1 = np.float32(biggest) # Getting points to warp from
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]]) # Getting points to warp to

matrix = cv2.getPerspectiveTransform(pts1, pts2)
cropped_image = cv2.warpPerspective(img, matrix, (width, height)) # Extracting the card blob
cv2.imshow("Final image after cropping", cropped_image)
cv2.waitKey(0)

cv2.imwrite("crop.jpg", cropped_image) # Saving image as "crop.jpg"
cv2.destroyAllWindows()