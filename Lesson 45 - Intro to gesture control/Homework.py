import cv2
import numpy as np

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam")
    exit()

points = []

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture image")
        break

    frame = cv2.flip(frame, 1)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)

    mask = cv2.inRange(hsv, lower_skin, upper_skin)

    result = cv2.bitwise_and(frame, frame, mask=mask)

    contours, _ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    if contours:
        max_contour = max(contours, key=cv2.contourArea)

        if cv2.contourArea(max_contour) > 500:
            x, y, w, h = cv2.boundingRect(max_contour)

            center_x = int(x + w / 2)
            center_y = int(y + h / 2)

            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

            cv2.circle(
                frame,
                (center_x, center_y),
                15,
                (0, 0, 255),
                -1
            )

            points.append((center_x, center_y))

            if len(points) > 1:
                for i in range(1, len(points)):
                    cv2.line(
                        frame,
                        points[i - 1],
                        points[i],
                        (255, 0, 0),
                        3
                    )

    cv2.putText(
        frame,
        "Move your hand to draw",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    cv2.putText(
        frame,
        "Press C to clear | Press Q to quit",
        (10, 60),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        2
    )

    cv2.imshow("Gesture Control", frame)
    cv2.imshow("Filtered Frame", result)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("c"):
        points = []

    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()