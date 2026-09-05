import cv2, time, pyautogui
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

SCROLL_SPEED = 300
SCROLL_DELAY = 0.15
CAM_WIDTH, CAM_HEIGHT = 680, 400

def detect_gesture(landmarks, handedness):
    fingers = []

    tips = [
        mp_hands.HandLandmark.INDEX_FINGER_TIP,
        mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
        mp_hands.HandLandmark.RING_FINGER_TIP,
        mp_hands.HandLandmark.PINKY_TIP
    ]

    for tip in tips:
        if landmarks.landmark[tip].y < landmarks.landmark[tip - 2].y:
            fingers.append(1)

    thumb_tip = landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    thumb_ip = landmarks.landmark[mp_hands.HandLandmark.THUMB_IP]

    if handedness == "Right":
        if thumb_tip.x > thumb_ip.x:
            fingers.append(1)
    else:
        if thumb_tip.x < thumb_ip.x:
            fingers.append(1)

    if len(fingers) == 5:
        return "scroll_up"
    elif len(fingers) == 0:
        return "scroll_down"
    else:
        return "none"

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, CAM_WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, CAM_HEIGHT)

last_scroll = 0

print("Gesture Scroll Control Active")
print("Open Palm: Scroll Up")
print("Closed Fist: Scroll Down")
print("Press 'q' to exit")

while cap.isOpened():
    success, img = cap.read()

    if not success:
        break

    img = cv2.flip(img, 1)

    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_img)

    gesture = "none"
    handedness = "unknown"

    if results.multi_hand_landmarks:
        hand = results.multi_hand_landmarks[0]

        if results.multi_handedness:
            handedness = results.multi_handedness[0].classification[0].label

        gesture = detect_gesture(hand, handedness)

        mp_drawing.draw_landmarks(
            img,
            hand,
            mp_hands.HAND_CONNECTIONS
        )

        current_time = time.time()

        if current_time - last_scroll >= SCROLL_DELAY:
            if gesture == "scroll_up":
                pyautogui.scroll(SCROLL_SPEED)
                last_scroll = current_time

            elif gesture == "scroll_down":
                pyautogui.scroll(-SCROLL_SPEED)
                last_scroll = current_time

    cv2.putText(
        img,
        "Gesture: " + gesture,
        (10, 35),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

    cv2.imshow("Gesture Scroll Control", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
hands.close()
cv2.destroyAllWindows()