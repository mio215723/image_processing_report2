import cv2 as cv
import sys

img = cv.imread(cv.samples.findFile("lena.jpeg"))
if img is None:
    sys.exit("Could not read the image.")
# 画像の大きさを取得
height, width, channels = img.shape[:3]
print("width: " + str(width))
print("height: " + str(height))
cv.imshow("Display window", img)
cv.waitKey(0)
