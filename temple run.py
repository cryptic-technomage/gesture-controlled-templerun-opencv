import cv2
import mediapipe as mp
import keyboard  

# Hand detection setup
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7,
    max_num_hands=2
)

# cv2 video setup
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

def index_finger_up(landmarks):
    return landmarks.landmark[8].y < landmarks.landmark[6].y # the value of y is normalized so lower value means the landmark is higher in image.

def all_five_fingers_up(landmarks):
    # check thumb up
    thumb_up = landmarks.landmark[4].x < landmarks.landmark[3].x
    # check index, middle, ring, pinky up
    fingers_up = []
    tips = [8, 12, 16, 20]
    pips = [6, 10, 14, 18]
    for tip, pip in zip(tips, pips):
        fingers_up.append(landmarks.landmark[tip].y < landmarks.landmark[pip].y)
    return thumb_up and all(fingers_up)

last_gesture = None

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    left_index_up = False
    right_index_up = False
    right_all_fingers_up = False

    if results.multi_hand_landmarks and results.multi_handedness:
        for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
            label = handedness.classification[0].label  # 'Left' or 'Right'
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            if label == "Left":
                if index_finger_up(hand_landmarks):
                    left_index_up = True
            elif label == "Right":
                if index_finger_up(hand_landmarks):
                    right_index_up = True
                if all_five_fingers_up(hand_landmarks):
                    right_all_fingers_up = True

    # gesture logic
    current_gesture = None
    if right_all_fingers_up:
        current_gesture = "jump"
    elif left_index_up and right_index_up:
        current_gesture = "down"
    elif left_index_up:
        current_gesture = "left"
    elif right_index_up:
        current_gesture = "right"

    # Trigger only on gesture change
    if current_gesture != last_gesture:
        if current_gesture == "left":
            keyboard.press_and_release("left")
            print("↩️ Turn Left")
        elif current_gesture == "right":
            keyboard.press_and_release("right")
            print("↪️ Turn Right")
        elif current_gesture == "down":
            keyboard.press_and_release("down")
            print("⬇️ Slide Down")
        elif current_gesture == "jump":
            keyboard.press_and_release("up")
            print("⬆️ Jump")
        last_gesture = current_gesture

    cv2.imshow("Temple Run Gesture Control", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
hands.close()
