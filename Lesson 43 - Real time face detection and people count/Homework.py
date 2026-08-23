import cv2
import numpy as np

def apply_effect(frame, effect):

    img = frame.copy()

    if effect == "original":
        img = frame.copy()

    elif effect == "rotate":
        img = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)

    elif effect == "crop":
        height, width = frame.shape[:2]

        x1 = width // 4
        y1 = height // 4
        x2 = width * 3 // 4
        y2 = height * 3 // 4

        img = frame[y1:y2, x1:x2]

    elif effect == "bright":
        img = cv2.convertScaleAbs(frame, alpha=1.0, beta=80)

    elif effect == "dark":
        img = cv2.convertScaleAbs(frame, alpha=1.0, beta=-80)

    return img


def main():

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Cannot open webcam.")
        return

    effect = "original"

    print("Press o for original")
    print("Press r for rotation")
    print("Press c for cropping")
    print("Press b for brightness")
    print("Press d for darker")
    print("Press q to quit")

    while True:

        ret, frame = cap.read()

        if not ret:
            print("Error: Failed to capture image.")
            break

        output = apply_effect(frame, effect)

        cv2.imshow("Image Manipulation", output)

        key = cv2.waitKey(1) & 0xFF

        if key == ord("o"):
            effect = "original"

        elif key == ord("r"):
            effect = "rotate"

        elif key == ord("c"):
            effect = "crop"

        elif key == ord("b"):
            effect = "bright"

        elif key == ord("d"):
            effect = "dark"

        elif key == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
    
main()