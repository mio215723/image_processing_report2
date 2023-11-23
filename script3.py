import cv2 as cv
import sys

def onMouse(event, x, y, flags, params):
    if event == cv.EVENT_LBUTTONDOWN:
        print(str(x) + "," + str(y))

img = cv.imread(cv.samples.findFile("lena.jpeg"))
if img is None:
    sys.exit("Could not read the image.")
cv.imshow("Display window", img)
cv.setMouseCallback("Display window", onMouse)
cv.waitKey(0)
