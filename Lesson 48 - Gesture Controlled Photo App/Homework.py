import cv2, time, numpy as np
import mediapipe as mp

H = mp.solutions.hands
TIP = H.HandLandmark

ids = {
    "thumb": TIP.THUMB_TIP,
    "index": TIP.INDEX_FINGER_TIP,
    "middle": TIP.MIDDLE_FINGER_TIP,
    "ring": TIP.RING_FINGER_TIP,
    "pinky": TIP.PINKY_TIP
}

hands = H.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
draw = mp.solutions.drawing_utils

pairs = {
    "middle": ("SEPIA", "NEGATIVE"),
    "ring": ("BLUR", "GLITCH"),
    "pinky": ("EDGE", "CARTOON")
}

st = {k: 0 for k in pairs}
cur = "SEPIA"

DEB, CAP, TT, TP = 0.6, 1.2, 30, 20
la = lc = 0
pinch_on = False

MAIN, POP = "Gesture-Controlled Photo App", "Captured(ESC / Close To Remove)"
paused = False
freeze = None

SEPIA_M = np.array([
    [0.272, 0.534, 0.131],
    [0.349, 0.686, 0.168],
    [0.393, 0.769, 0.189]
])

def apply(img, t):
    if t == "SEPIA":
        return np.clip(cv2.transform(img, SEPIA_M), 0, 255).astype(np.uint8)

    if t == "NEGATIVE":
        return cv2.bitwise_not(img)

    if t == "BLUR":
        return cv2.GaussianBlur(img, (15, 15), 0)

    if t == "GLITCH":
        h, w = img.shape[:2]
        r = img[:, :, 2]
        g = img[:, :, 1]
        b = img[:, :, 0]
        return cv2.merge([
            np.roll(b, -int(0.02 * w), axis=1),
            g,
            np.roll(r, int(0.04 * w), axis=1)
        ])

    if t == "EDGE":
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return cv2.Canny(gray, 80, 160)

    if t == "CARTOON":
        g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        e = cv2.adaptiveThreshold(
            cv2.medianBlur(g, 7),
            255,
            cv2.ADAPTIVE_THRESH_MEAN_C,
            cv2.THRESH_BINARY,
            9,
            2
        )
        c = cv2.bilateralFilter(img, 9, 75, 75)
        return cv2.bitwise_and(c, c, mask=e)

    return img

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not access the webcam.")
    exit()

cv2.namedWindow(MAIN, cv2.WINDOW_NORMAL)

while True:
    if paused:
        cv2.imshow(MAIN, freeze)
        k = cv2.waitKey(50) & 0xFF

        if k == ord("q"):
            break

        if k == 27:
            paused = False
            pinch_on = False
            try:
                cv2.destroyWindow(POP)
            except:
                pass
            continue

    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    now = time.time()

    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:
            draw.draw_landmarks(frame, hand, H.HAND_CONNECTIONS)

            p = {}

            for name, landmark in ids.items():
                x = int(hand.landmark[landmark].x * frame.shape[1])
                y = int(hand.landmark[landmark].y * frame.shape[0])
                p[name] = (x, y)

            thumb = np.array(p["thumb"])
            index = np.array(p["index"])
            middle = np.array(p["middle"])
            ring = np.array(p["ring"])
            pinky = np.array(p["pinky"])

            ti = np.linalg.norm(thumb - index)
            tm = np.linalg.norm(thumb - middle)
            tr = np.linalg.norm(thumb - ring)
            tp = np.linalg.norm(thumb - pinky)

            if ti < TT:
                if not pinch_on and now - lc > CAP:
                    freeze = apply(frame.copy(), cur)
                    paused = True
                    pinch_on = True
                    lc = now

                    cv2.imshow(POP, freeze)

            else:
                pinch_on = False

            if tm < TP:
                if now - st["middle"] > DEB:
                    if cur == pairs["middle"][0]:
                        cur = pairs["middle"][1]
                    else:
                        cur = pairs["middle"][0]
                    st["middle"] = now

            if tr < TP:
                if now - st["ring"] > DEB:
                    if cur == pairs["ring"][0]:
                        cur = pairs["ring"][1]
                    else:
                        cur = pairs["ring"][0]
                    st["ring"] = now

            if tp < TP:
                if now - st["pinky"] > DEB:
                    if cur == pairs["pinky"][0]:
                        cur = pairs["pinky"][1]
                    else:
                        cur = pairs["pinky"][0]
                    st["pinky"] = now

    cv2.putText(
        frame,
        "Filter: " + cur,
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 255),
        2
    )

    cv2.putText(
        frame,
        "Thumb + Index = Capture",
        (20, 75),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.65,
        (255, 255, 255),
        2
    )

    cv2.putText(
        frame,
        "Thumb + Middle/Ring/Pinky = Change Filter",
        (20, 105),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.55,
        (255, 255, 255),
        2
    )

    cv2.imshow(MAIN, frame)

    k = cv2.waitKey(1) & 0xFF

    if k == ord("q") or k == 27:
        break

cap.release()
hands.close()
cv2.destroyAllWindows()