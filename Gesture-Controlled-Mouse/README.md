# ✋ Gesture-Controlled Mouse

This project enables **hands-free mouse interaction** using real-time hand gesture recognition via **OpenCV**, **MediaPipe**, and **PyAutoGUI**. With just a webcam, users can control the mouse cursor, perform left/right clicks, double-clicks, and even drag or select text—all using intuitive finger movements.

---

## 🚀 Features

- 🖐️ **Hand Detection**  
  Uses MediaPipe's hand-tracking model to identify and track hand landmarks in real time.

- 🤌 **Gesture Recognition**  
  Detects specific gestures such as:
  - Thumb + Index → Left Click
  - Thumb + Pinky → Right Click
  - Rapid Thumb + Index Taps → Double Click

- 🖱️ **Text Selection and Dragging**  
  Pinch gestures trigger selection, and smooth motion allows dragging of selected content.

---

## 🧰 Requirements

- Python 3.x
- `opencv-python`
- `mediapipe`
- `pyautogui`

Install all dependencies with:

```bash
pip install opencv-python mediapipe pyautogui
````

---

## ▶️ Usage

1. Clone the repository:

```bash
git clone https://github.com/VipranshOjha/GestureControlledMouse.git
cd GestureControlledMouse
```

2. Run the script:

```bash
python hand_gesture_control.py
```

3. Control your mouse with gestures:

   * 👆 **Left Click**: Bring thumb and index finger tips close together.
   * 🤙 **Right Click**: Bring thumb and pinky tips together.
   * ✌️ **Double Click**: Rapid double pinch using thumb and index finger.
   * 📄 **Select Text**: Pinch thumb and index, hold, then drag.
   * 🧲 **Drag Objects**: Hold a left-click pinch and move your hand.

4. Press `q` to quit the application.

---

## ⚙️ Customization

You can tweak gesture detection sensitivity inside the script:

| Parameter                        | Purpose                              |
| -------------------------------- | ------------------------------------ |
| `thumb_index_distance_threshold` | Distance to trigger left-click       |
| `thumb_pinky_distance_threshold` | Distance to trigger right-click      |
| `double_click_threshold`         | Max time between double-tap clicks   |
| `text_selection_threshold`       | Controls precision of text selection |

---

## 📌 Use Cases

* Accessibility and assistive technologies
* Smart desktops and touchless interfaces
* Experimental HCI projects using vision-based control

---

## 🙌 Contributions

Pull requests, suggestions, and new features are welcome!
Feel free to fork the repo and extend the gesture set or add enhancements.

---
