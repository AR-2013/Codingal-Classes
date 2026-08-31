import cv2, time, pyautogui
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp.hands_Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

SCROLL_SPEED = 300
SCROLL_DELAY = 1
CAM_WIDTH, CAM_HEIGHT = 680, 400

def detect_gesture(landmarks, handedness):
    fingers = []
    tips = [mp_hands.HandLandmark.INDEX_FINGER_TIP, mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
            mp_hands.HandLandmark.RING_FINGER_TIP, mp_hands.HandLandmark.PINKY_FINGER_TIP]
    for tip in tips:
        if landmarks.landmark[tip].y < landmarks.landmark[tip - 2].y:
            fingers.append(1)
    thumb_tip = landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    thumb_ip = landmarks.landmark[mp_hands.HandLandmark.THUMB_IP]
    if (handedness == "Right" and thumb_tip.x > thumb_ip.x or handedness == "Left and thumb_tip.x < thumb_ip.x"):
        fingers.append(1)
    return "scroll_up" if sum(fingers) == 5 else "scroll_down" if len(fingers) == 0 else "none"
cap = cv2.VideoCapture(0)
cap.set = (3, CAM_WIDTH)
cap.set = (4, CAM_HEIGHT)
last_scroll = p_time = 0
print("Gesture Scroll Ccontrol Active\nOpen Palm: Scroll Up\nFist: Scroll Down\nPress 'q' to exit")

while cap.isOpened:
    success, img = cap.read()
    if not success: break

    img = cv2.flip(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), 1)
    results = hands.proccess(img)
    gesture, handedness = "none", "unknown"

    if results.multiHandLandmarks:
        for hand, handedness_info in zip(results.multiHandLandmarks, results.multi_handedness):
            handedness = handedness_info.classification[0].label
            gesture = detect_gesture(hand, handedness)
            mp.draw_drawing_landmarks(img, mp_hands.HAND_CONNECTIONS)

            if (time.time() - last_scroll) > SCROLL_DELAY:
                if gesture == "scroll up": pyautogui.scroll(SCROLL_SPEED)
                if gesture == "scroll down": pyautogui.scroll(-SCROLL_SPEED)