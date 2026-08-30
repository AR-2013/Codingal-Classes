import cv2
import mediapipe as mp
import numpy as np
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import screen_brightness_control as sbc

Hands = mp.solutions.hands

hands = Hands.Hands(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

draw = mp.solutions.drawing_utils

TH = Hands.HandLandmark.THUMB_TIP
IX = Hands.HandLandmark.INDEX_FINGER_TIP

try:
    dev = (
        AudioUtilities.GetDefaultOutputDevice()
        if hasattr(AudioUtilities, "GetDefaultOutputDevice")
        else AudioUtilities.GetSpeakers()
    )

    volctl = dev.EndpointVolume.QueryInterface(IAudioEndpointVolume)

    minv, maxv = volctl.GetVolumeRange()[:2]

except Exception as e:
    print(f"Pycaw error: {e}")
    exit()

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error! Webcam not accessible.")
    exit()

WIN = "Hand Gesture Control"
cv2.namedWindow(WIN, cv2.WINDOW_NORMAL)

while True:

    ok, img = cap.read()

    if not ok:
        break

    img = cv2.flip(img, 1)

    h, w = img.shape[:2]

    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    res = hands.process(rgb)

    if res.multi_hand_landmarks and res.multi_handedness:

        for i, hand in enumerate(res.multi_hand_landmarks):

            label = res.multi_handedness[i].classification[0].label

            draw.draw_landmarks(
                img,
                hand,
                Hands.HAND_CONNECTIONS
            )

            lm = hand.landmark

            tp = (
                int(lm[TH].x * w),
                int(lm[TH].y * h)
            )

            ip = (
                int(lm[IX].x * w),
                int(lm[IX].y * h)
            )

            distance = np.hypot(
                ip[0] - tp[0],
                ip[1] - tp[1]
            )

            cv2.circle(
                img,
                tp,
                10,
                (255, 0, 0),
                cv2.FILLED
            )

            cv2.circle(
                img,
                ip,
                10,
                (255, 0, 0),
                cv2.FILLED
            )

            cv2.line(
                img,
                tp,
                ip,
                (255, 0, 0),
                3
            )

            if label == "Left":

                volume = np.interp(
                    distance,
                    [20, 200],
                    [minv, maxv]
                )

                volctl.SetMasterVolumeLevel(volume, None)

                volume_percent = np.interp(
                    volume,
                    [minv, maxv],
                    [0, 100]
                )

                cv2.putText(
                    img,
                    f"Volume: {int(volume_percent)}%",
                    (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0),
                    2
                )

            elif label == "Right":

                brightness = int(
                    np.interp(
                        distance,
                        [20, 200],
                        [0, 100]
                    )
                )

                try:
                    sbc.set_brightness(brightness)
                except Exception:
                    pass

                cv2.putText(
                    img,
                    f"Brightness: {brightness}%",
                    (30, 90),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 255),
                    2
                )

            cv2.putText(
                img,
                f"{label} Hand",
                (30, h - 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 255, 255),
                2
            )

    cv2.putText(
        img,
        "Left hand = Volume | Right hand = Brightness",
        (30, h - 20),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        2
    )

    cv2.imshow(WIN, img)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q") or key == 27:
        break

cap.release()
cv2.destroyAllWindows()
hands.close()