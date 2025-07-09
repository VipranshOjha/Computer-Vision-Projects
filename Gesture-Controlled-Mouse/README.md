# Gesture Control with OpenCV and MediaPipe

This project demonstrates real-time gesture control using OpenCV and MediaPipe libraries in Python. By leveraging the webcam feed, it allows users to interact with their computer screen through gestures, enabling actions like left-click, right-click, and double-click, as well as text selection and dragging.

## Features

- **Hand Detection:** Utilizes the MediaPipe Hands model to detect and track hand landmarks in real-time from the webcam feed.
- **Gesture Recognition:** Recognizes specific hand gestures such as thumb-index distance for left-click, thumb-pinky distance for right-click, and double-click detection.
- **Text Selection:** Enables users to select text on the screen by bringing their thumb tip close to their index finger tip.
- **Dragging:** Allows users to drag selected text or objects on the screen by holding down the left-click gesture while moving their hand.

## Requirements

- Python 3.x
- OpenCV
- MediaPipe
- PyAutoGUI

## Installation

1. Clone the repository:

```bash
git clone https://github.com/VipranshOjha/GestureControlledMouse.git
```

2. Install dependencies:

```bash
pip install opencv-python mediapipe pyautogui
```

## Usage

1. Run the script:

```bash
python hand_gesture_control.py
```

2. Position your hand in front of the webcam.
3. Perform gestures according to the specified actions:
   - Thumb and index finger close together for left-click.
   - Thumb and pinky finger close together for right-click.
   - Thumb and index finger tips close together for text selection.
   - Double-click by quickly tapping thumb and index finger tips twice.
   - Drag by selecting text or object and moving your hand while holding down left-click gesture.
4. Press 'q' to quit the application.

## Customization

- Adjust distance thresholds (`thumb_index_distance_threshold`, `thumb_pinky_distance_threshold`) for gesture recognition as per your preference.
- Modify `double_click_threshold` to change the time window for double-click detection.
- Update `text_selection_threshold` to adjust the sensitivity for text selection.

---

## Contributions

Contributions are welcome! Feel free to open issues or pull requests for bug fixes, improvements, or new features.

## Acknowledgments

- Thanks to the developers of OpenCV and MediaPipe for providing powerful tools for computer vision applications.
- Special thanks to the contributors of PyAutoGUI for simplifying GUI automation tasks.

---
