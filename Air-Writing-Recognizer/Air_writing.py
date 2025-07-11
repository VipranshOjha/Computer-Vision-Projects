import cv2
import mediapipe as mp

from collections import deque
import math

class AirWritingRecognizer:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.5
        )
        self.mp_drawing = mp.solutions.drawing_utils

        self.trajectory_points = deque(maxlen=100)
        self.is_writing = False
        self.letter_trajectory = []
        self.last_position = None
        self.recognized_text = ""
        self.templates = self._initialize_templates()

    def _initialize_templates(self):
        return {
            'A': [(0, 100), (50, 0), (100, 100), (25, 50), (75, 50)],
            'B': [(0, 0), (0, 100), (75, 75), (75, 25), (0, 50)],
            'C': [(100, 25), (50, 0), (0, 25), (0, 75), (50, 100), (100, 75)],
            'D': [(0, 0), (0, 100), (75, 75), (100, 50), (75, 25)],
            'E': [(100, 0), (0, 0), (0, 50), (50, 50), (0, 100), (100, 100)],
            'F': [(0, 0), (100, 0), (0, 50), (50, 50), (0, 100)],
            'G': [(100, 25), (50, 0), (0, 25), (0, 75), (50, 100), (100, 75), (100, 50)],
            'H': [(0, 0), (0, 100), (0, 50), (100, 50), (100, 100), (100, 0)],
            'I': [(50, 0), (50, 100)],
            'J': [(100, 0), (100, 100), (50, 100), (25, 75)],
            'K': [(0, 0), (0, 100), (50, 50), (100, 0), (50, 50), (100, 100)],
            'L': [(0, 0), (0, 100), (100, 100)],
            'M': [(0, 100), (25, 0), (50, 50), (75, 0), (100, 100)],
            'N': [(0, 100), (0, 0), (100, 100), (100, 0)],
            'O': [(50, 0), (25, 25), (0, 50), (25, 75), (50, 100), (75, 75), (100, 50), (75, 25), (50, 0)],
            'P': [(0, 0), (0, 100), (50, 100), (75, 75), (50, 50), (0, 50)],
            'Q': [(50, 0), (25, 25), (0, 50), (25, 75), (50, 100), (75, 75), (100, 50), (75, 25), (50, 0), (75, 100)],
            'R': [(0, 0), (0, 100), (50, 100), (75, 75), (50, 50), (0, 50), (100, 0)],
            'S': [(100, 25), (75, 0), (25, 0), (0, 25), (50, 50), (100, 75), (75, 100), (25, 100), (0, 75)],
            'T': [(50, 0), (50, 100), (0, 0), (100, 0)],
            'U': [(0, 0), (0, 100), (50, 100), (100, 100), (100, 0)],
            'V': [(0, 0), (50, 100), (100, 0)],
            'W': [(0, 0), (25, 100), (50, 50), (75, 100), (100, 0)],
            'X': [(0, 0), (100, 100), (50, 50), (0, 100), (100, 0)],
            'Y': [(50, 0), (50, 50), (0, 100), (50, 50), (100, 100)],
            'Z': [(0, 0), (100, 0), (0, 100), (100, 100)]
        }

    def recognize_letter(self, points):
        if len(points) < 5:
            return None

        min_x = min(p[0] for p in points)
        max_x = max(p[0] for p in points)
        min_y = min(p[1] for p in points)
        max_y = max(p[1] for p in points)

        width = max(max_x - min_x, 1)
        height = max(max_y - min_y, 1)

        normalized_points = [
            ((p[0] - min_x) * 100 // width, (p[1] - min_y) * 100 // height)
            for p in points
        ]

        best_match = None
        best_score = float('inf')

        for letter, template in self.templates.items():
            score = self._calculate_matching_score(normalized_points, template)
            if score < best_score:
                best_score = score
                best_match = letter

        return best_match if best_score < 2000 else None

    def _calculate_matching_score(self, points, template):
        resampled_points = self._resample_points(points, 20)
        resampled_template = self._resample_points(template, 20)

        score = sum(
            math.sqrt((p[0] - t[0]) ** 2 + (p[1] - t[1]) ** 2)
            for p, t in zip(resampled_points, resampled_template)
        )
        return score

    def _resample_points(self, points, n_points):
        if len(points) <= 1:
            return points * n_points

        path_length = sum(
            math.sqrt((points[i][0] - points[i - 1][0]) ** 2 + (points[i][1] - points[i - 1][1]) ** 2)
            for i in range(1, len(points))
        )

        if path_length == 0:
            return points[:1] * n_points

        interval = path_length / (n_points - 1)

        resampled = [points[0]]
        current_distance = 0
        i = 1

        while len(resampled) < n_points and i < len(points):
            p1 = points[i - 1]
            p2 = points[i]
            segment_length = math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

            if current_distance + segment_length >= interval:
                t = (interval - current_distance) / segment_length
                new_x = int(p1[0] + t * (p2[0] - p1[0]))
                new_y = int(p1[1] + t * (p2[1] - p1[1]))
                resampled.append((new_x, new_y))
                points.insert(i, (new_x, new_y))
                current_distance = 0
            else:
                current_distance += segment_length
                i += 1

        while len(resampled) < n_points:
            resampled.append(points[-1])

        return resampled

    def detect_gesture(self, hand_landmarks):
        index_tip = hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP]
        middle_tip = hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
        thumb_tip = hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_TIP]

        index_thumb_dist = math.sqrt((index_tip.x - thumb_tip.x) ** 2 + (index_tip.y - thumb_tip.y) ** 2)
        middle_thumb_dist = math.sqrt((middle_tip.x - thumb_tip.x) ** 2 + (middle_tip.y - thumb_tip.y) ** 2)

        if index_thumb_dist < 0.05:
            self.is_writing = True
            self.letter_trajectory.clear()
        elif middle_thumb_dist < 0.05:
            self.is_writing = False
            if self.letter_trajectory:
                recognized_letter = self.recognize_letter(self.letter_trajectory)
                if recognized_letter:
                    self.recognized_text += recognized_letter
                self.letter_trajectory.clear()

        return self.is_writing


recognizer = AirWritingRecognizer()
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = recognizer.hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            recognizer.mp_drawing.draw_landmarks(frame, hand_landmarks, recognizer.mp_hands.HAND_CONNECTIONS)
            if recognizer.detect_gesture(hand_landmarks):
                fingertip = (
                int(hand_landmarks.landmark[8].x * frame.shape[1]), int(hand_landmarks.landmark[8].y * frame.shape[0]))
                recognizer.letter_trajectory.append(fingertip)
                for i in range(1, len(recognizer.letter_trajectory)):
                    cv2.line(frame, recognizer.letter_trajectory[i - 1], recognizer.letter_trajectory[i], (0, 255, 0),
                             2)

    cv2.putText(frame, recognizer.recognized_text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Air Writing", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
