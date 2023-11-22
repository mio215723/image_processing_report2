import cv2 as cv
import sys
img = cv.imread(cv.samples.findFile("lena.jpeg"))
if img is None:
    sys.exit("Could not read the image.")
cv.imshow("Display window", img)
cv.waitKey(0)