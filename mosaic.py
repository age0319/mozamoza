import cv2


# imgは元画像、rectはモザイクをかける座標
def put_mosaic(img, rect):
    # 縮小するサイズ
    size = (10, 10)

    # モザイクをかける座標を取得、左上(x1,y1),右下(x2,y2)
    (x1, y1, x2, y2) = rect

    # モザイクをかける幅と高さ
    w = x2 - x1
    h = y2 - y1

    # モザイクをかける部分を元画像から切り取り
    area = img[y1:y2, x1:x2]

    # 縮小
    small = cv2.resize(area, size)

    # 縮小した画像を拡大,zoomにはモザイク画像が入る
    zoom = cv2.resize(small, (w, h), interpolation=cv2.INTER_AREA)

    # 元の画像へモザイク画像をコピー
    img2 = img.copy()
    img2[y1:y2, x1:x2] = zoom

    return img2
