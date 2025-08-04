import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands  # type: ignore
mp_draw = mp.solutions.drawing_utils  # type: ignore

hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

tip_ids = [4, 8, 12, 16, 20]  # Thumb, Index, Middle, Ring, Pinky

cap = cv2.VideoCapture(0)

prev_gesture = ""

while cap.isOpened():
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(img_rgb)

    gesture = ""

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            landmarks = hand_landmarks.landmark
            h, w, _ = img.shape

            fingers = []

            # Thumb
            if landmarks[tip_ids[0]].x < landmarks[tip_ids[0] - 1].x:
                fingers.append(1)
            else:
                fingers.append(0)

            # Other fingers
            for i in range(1, 5):
                if landmarks[tip_ids[i]].y < landmarks[tip_ids[i] - 2].y:
                    fingers.append(1)
                else:
                    fingers.append(0)

            if fingers == [0, 0, 0, 0, 0]: 
                gesture = "Help"
            elif fingers == [1, 1, 1, 1, 1]:
                gesture = "Open Hand"
            elif fingers == [1, 0, 0, 0, 0]:
                gesture = "Thumbs Up"
            elif fingers == [0, 1, 0, 0, 0]:
                gesture = "Pointing Up"
            elif fingers == [0, 1, 1, 0, 0]:
                gesture = "Peace"
            elif fingers == [0, 1, 1, 1, 1]:
                gesture = "Four Fingers Up"
            elif fingers == [0, 0, 0, 0, 1]:
                gesture = "Pinky Up"
            elif fingers == [0, 1, 0, 0, 1]:
                gesture = "Rock"
            elif fingers == [0, 0, 1, 0, 0]:
                gesture = "Middle Finger Up"
            elif fingers == [0, 0, 0, 1, 0]:
                gesture = "Ring Finger Up"
            elif fingers == [0, 0, 1, 1, 1]:
                gesture = "Nice"
            else:
                gesture = f"Gesture: {fingers}"

            if gesture != prev_gesture:
                print(f"Fingers status (thumb to pinky): {fingers}")
                print(gesture)
                prev_gesture = gesture

    # Subtitle drawing (always runs, even if no hand is detected)
    h, w, _ = img.shape
    font_scale = 1.2
    thickness = 3
    font = cv2.FONT_HERSHEY_SIMPLEX

    (text_width, text_height), _ = cv2.getTextSize(gesture, font, font_scale, thickness)
    text_x = int((w - text_width) / 2)
    text_y = h - 50

    cv2.rectangle(img, (text_x - 20, text_y - text_height - 20),
                  (text_x + text_width + 20, text_y + 10), (255, 255, 255), -1)

    cv2.putText(img, gesture, (text_x, text_y), font, font_scale, (0, 0, 0), thickness)

    cv2.imshow("Hand Gesture Recognition", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
