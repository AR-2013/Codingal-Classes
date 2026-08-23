import cv2
import numpy as np

def apply_filter(image, ftype):

    img = image.copy()

    if ftype == "original":
        img = image.copy()

    elif ftype == "red_tint":
        img[:, :, 0] = 0
        img[:, :, 1] = 0

    elif ftype == "green_tint":
        img[:, :, 0] = 0
        img[:, :, 2] = 0

    elif ftype == "blue_tint":
        img[:, :, 0] = 0
        img[:, :, 1] = 0

    elif ftype == "sobel":
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        sx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
        sy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

        sx = cv2.convertScaleAbs(sx)
        sy = cv2.convertScaleAbs(sy)

        sob = cv2.bitwise_or(sx, sy)

        img = cv2.cvtColor(sob, cv2.COLOR_GRAY2BGR)

    elif ftype == "canny":
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        can = cv2.Canny(gray, 100, 200)

        img = cv2.cvtColor(can, cv2.COLOR_GRAY2BGR)

    elif ftype == "cartoon":
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, 5)

        edges = cv2.adaptiveThreshold(
            gray,
            255,
            cv2.ADAPTIVE_THRESH_MEAN_C,
            cv2.THRESH_BINARY,
            9,
            9
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

    print("Press r for red tint")
    print("Press g for green tint")
    print("Press b for blue tint")
    print("Press s for Sobel edge detection")
    print("Press c for Canny edge detection")
    print("Press t for cartoon filter")
    print("Press o for original camera")
    print("Press q to quit")

    while True:

        ret, frame = cap.read()

        if not ret:
            print("Can't receive frame")
            break

        out = apply_filter(frame, ftype)

        cv2.imshow("Real-Time Image Filters", out)

        key = cv2.waitKey(1) & 0xFF

        if key == ord("r"):
            ftype = "red_tint"

        elif key == ord("g"):
            ftype = "green_tint"

        elif key == ord("b"):
            ftype = "blue_tint"

        elif key == ord("s"):
            ftype = "sobel"

        elif key == ord("c"):
            ftype = "canny"

        elif key == ord("t"):
            ftype = "cartoon"

        elif key == ord("o"):
            ftype = "original"

        elif key == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


main()