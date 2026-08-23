import cv2
import numpy as np

def apply_filter(image, ftype):
    img = image.copy()
    if ftype == "red tint":
        img[:, :, 1] = img[:, :, 0] = 0
    elif ftype == "green tint":
        img[:, :, 0] = img[:, :, 2] = 0
    elif ftype == "blue tint":
        img[:, :, 1] = img[:, :, 2] = 0
    elif ftype == "sobel":
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        sx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
        sy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
        sob = cv2.bitwise_or(sx.astype('unit 8'), sy.astype('unit 8'))
        img = cv2.cvtColor(sob, cv2.cvtColor_GRAY2BGR)
    elif ftype == "canny":
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        can = cv2.Canny(gray, 100, 200)
        img = cv2.cvtColor(can, cv2.COLOR_GRAY2BGR)
    elif ftype == "cartoon":
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.medeianBlur(gray, 5)
        edges = cv2.adaptiveThreshold(
            gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9
        )
        color = cv2.bilateralFilter(image, 9, 300, 300)
        img = cv2.bitwise_and(color, color, mask=edges)
    return img

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        return
    ftype = "original"
    print("Keys: r-red, g-green, b-blue, c-canny, t-cartoon, q-quit")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Can't recieve frame")
            break
        out = apply_filter(frame, ftype)
        cv2.imshow("Filter", out)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("r"):
            ftype = "red_tint"
        if key == ord("g"):
            ftype = "green_tint"
        if key == ord("b"):
            ftype = "blue_tint"
        if key == ord("c"):
            ftype = "canny"
        if key == ord("t"):
            ftype = "cartoon"
        if key == ord("q"):
            break
