import cv2
import mediapipe as mp 

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
# Start the webcam feed
cap = cv2.VideoCapture(0)

# Set up the hand detector
with mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5) as hands:
    while True:
        ret, frame = cap.read()
        
        if not ret:
            break
        
        frame = cv2.flip(frame, 1)
        
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        
        results = hands.process(rgb_frame)
        
        if results.multi_hand_landmarks:
            for hand_landmark in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmark, mp_hands.HAND_CONNECTIONS)
                
        cv2.imshow("Hand gesture Recognition", frame)
        
        key = cv2.waitKey(1)
        if key == 27:
            break
        
cap.release()
cv2.destroyAllWindows()