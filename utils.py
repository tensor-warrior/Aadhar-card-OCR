# Critical code. Please don't touch!
import cv2
import numpy as np

def reorder(points): 
    points = points.reshape((4, 2))
   
    points_new = np.zeros((4, 1, 2), dtype = np.int32)
    add = points.sum(1)
 
    points_new[0] = points[np.argmin(add)]
    points_new[3] = points[np.argmax(add)]
    
    diff = np.diff(points, axis=1)
    
    points_new[1] = points[np.argmin(diff)]
    points_new[2] = points[np.argmax(diff)]
 
    return points_new


def biggestContour(contours):
    biggest = np.array([])
    max_area = 0

    for i in contours:
        area = cv2.contourArea(i)

        if area > 5000:
            peri = cv2.arcLength(i, True)
            approx = cv2.approxPolyDP(i, 0.02 * peri, True)

            if area > max_area and len(approx) == 4:
                biggest = approx
                max_area = area

    return biggest, max_area


def drawRectangle(img,biggest,thickness):
    cv2.line(img, (biggest[0][0][0], biggest[0][0][1]), (biggest[1][0][0], biggest[1][0][1]), (0, 255, 0), thickness)
    cv2.line(img, (biggest[0][0][0], biggest[0][0][1]), (biggest[2][0][0], biggest[2][0][1]), (0, 255, 0), thickness)
    cv2.line(img, (biggest[3][0][0], biggest[3][0][1]), (biggest[2][0][0], biggest[2][0][1]), (0, 255, 0), thickness)
    cv2.line(img, (biggest[3][0][0], biggest[3][0][1]), (biggest[1][0][0], biggest[1][0][1]), (0, 255, 0), thickness)
 
    return img