import cv2
import mediapipe as mp
import pyautogui

# Initialize video capture
cap = cv2.VideoCapture(0)

# Initialize MediaPipe Hands
hand_detector = mp.solutions.hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
drawing_utils = mp.solutions.drawing_utils

# Get screen dimensions for mouse control
screen_width, screen_height = pyautogui.size()

while True:
    # Read a frame from the video capture
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame horizontally for a mirror effect
    frame = cv2.flip(frame, 1)

    # Convert the BGR frame to RGB for processing with MediaPipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with MediaPipe Hands
    results = hand_detector.process(rgb_frame)

    # Check if hand landmarks are detected
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw hand landmarks on the frame
            drawing_utils.draw_landmarks(frame, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)

            # Get coordinates of index fingertip and thumb tip
            index_x, index_y = int(hand_landmarks.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP].x * frame.shape[1]), \
                               int(hand_landmarks.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP].y * frame.shape[0])
            thumb_x, thumb_y = int(hand_landmarks.landmark[mp.solutions.hands.HandLandmark.THUMB_TIP].x * frame.shape[1]), \
                               int(hand_landmarks.landmark[mp.solutions.hands.HandLandmark.THUMB_TIP].y * frame.shape[0])

            # Perform actions based on hand position
            if abs(index_y - thumb_y) < 80:
                pyautogui.click()
                pyautogui.sleep(1)
            elif abs(index_y - thumb_y) < 200:
                pyautogui.moveTo(int(index_x * screen_width / frame.shape[1]), int(index_y * screen_height / frame.shape[0]))

    # Display the processed frame
    cv2.imshow('Finger Controlled Mouse', frame)

    # Check for 'q' key press to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()
