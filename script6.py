import cv2 as cv

# グローバル変数
drawing = False  # マウスがドラッグ中かどうかを示すフラグ
ix, iy = -1, -1  # ドラッグの開始座標

# マウスイベントのコールバック関数
def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing

    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        cv.rectangle(img, (ix, iy), (x, y), (0, 255, 255), 2)  # 黄色の矩形を描画
        cv.imshow("Image", img)

# 画像の読み込み
img = cv.imread(cv.samples.findFile("lena.jpeg"))
cv.imshow("Image", img)

# マウスイベントのコールバック関数の設定
cv.setMouseCallback("Image", draw_rectangle)
key = cv.waitKey(0)
