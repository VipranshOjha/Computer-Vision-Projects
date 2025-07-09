# 🧠 Multi-Modal Mouse

**Multi-Modal Mouse** is an advanced hands-free input system that combines **eye tracking** and **hand gesture recognition** into a seamless, intuitive interface. It enables users to control the mouse cursor and perform click or scroll actions using either **eye movement** or **hand gestures**—or both.

---

## 🚀 Features

- 👁️ **Eye Tracking for Cursor Movement**  
  Uses real-time gaze direction to control the position of the cursor.

- ✋ **Gesture Recognition for Click & Scroll**  
  Detects hand movements (e.g., finger pinch or spread) to trigger left/right clicks and scrolling actions.

- 🔁 **Multi-Modal Fusion**  
  Combines both input methods fluidly for more accurate and natural interaction.

- ⚡ **Real-Time Performance**  
  Built with `OpenCV`, `MediaPipe`, and `PyAutoGUI` for efficient, real-time responsiveness.

---

## 🧰 Dependencies

Install the required Python libraries:

```
pip install opencv-python mediapipe pyautogui
````

---

## ▶️ How to Run

Make sure your webcam is active and run the script:

```
python MultiModalMouse.py
```

> ⚠️ Ensure good lighting and a clear background for optimal gesture and gaze detection.

---

## 🖱️ Controls

| Input Method        | Action              |
| ------------------- | ------------------- |
| Eye Movement        | Move the cursor     |
| Thumb + Index       | Left-click gesture  |
| Thumb + Pinky       | Right-click gesture |
| Finger Pinch + Hold | Scroll or select    |

---

## 📌 Use Cases

* Accessibility and assistive technology
* Smart desktops and human-computer interaction (HCI)
* Hands-free control in cleanrooms or medical environments

---

## ⚙️ Customization

You can adjust:

* **Sensitivity** for cursor movement
* **Gesture distance thresholds**
* **Click delay timers**

All parameters are easily modifiable within `MultiModalMouse.py`.

---

## 🙌 Contributions

Suggestions, improvements, and pull requests are welcome!
Feel free to fork and experiment with new gesture mappings or gaze models.

---
