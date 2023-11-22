import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread(cv.samples.findFile("lena.jpeg"), cv.IMREAD_GRAYSCALE)
hist = cv.calcHist([img], [0], None, [256], [0, 256])

# グラフの描画
plt.plot(hist)
plt.title('Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.show()