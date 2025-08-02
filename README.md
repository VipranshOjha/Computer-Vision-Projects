# 🧠 Computer Vision Projects

This repository is a collection of real-time human-computer interaction systems developed using **Python**, **OpenCV**, **MediaPipe**, and related libraries. Each project showcases a unique way to control a computer using **hand gestures**, **eye tracking**, or a combination of both—demonstrating the power of computer vision for accessibility, touchless control, and experimental UI/UX.

---

## 📂 Projects Included

### 1. ✋ [Gesture-Controlled Mouse](./Gesture-Controlled-Mouse)
Control your computer using hand gestures captured via webcam.

**Key Features:**
- Hand tracking via MediaPipe
- Left/right clicks with thumb-index or thumb-pinky gestures
- Double-click and drag using custom pinch-based logic

---

### 2. 👁️ [Gaze-Controlled Mouse](./Gaze-Controlled-Mouse)
A hands-free system using **eye movement and blinking** to control the mouse.

**Key Features:**
- Cursor moves with gaze direction
- Blinks mapped to clicks
- Real-time performance using `OpenCV` and `dlib`

---

### 3. 🧠 [Multi-Modal Mouse](./Multi-Modal-Mouse)
An advanced hybrid system combining both eye tracking and hand gestures.

**Key Features:**
- Gaze-based cursor movement
- Gesture-based click and scroll controls
- Seamless switching between input modes

---

### 4. ✍️ [Air-Writing Recognizer](https://github.com/VipranshOjha/Computer-Vision-Projects/tree/main/Air-Writing-Recognizer)
Draw letters in the air using your index finger and have them recognized in real time.

**Key Features:**
- Real-time hand tracking using MediaPipe
- Write by touching index finger to thumb, and stop with middle finger
- Matches finger trajectory to letter templates (A–Z)
- Displays live recognized text without requiring a neural network

---

### 5. 🔒 [Auto Screen Lock](https://github.com/VipranshOjha/Daily-Problem-Solvers/tree/main/Auto-Screen-Lock)
Automatically locks your screen when you leave your desk! Uses your webcam to detect if you're present and locks the computer after a set timeout if you're not—protecting your files and privacy effortlessly.

**Key Features:**
- Face detection via webcam (OpenCV)
- Customizable timeout before locking
- Lightweight, runs quietly in the background
- Cross-platform: supports Windows, Mac, and Linux

---

## 🧰 Setup & Installation

Each project contains its own `README.md` with installation instructions and usage examples. All scripts are written in **Python 3.x** and require libraries like:

```bash
pip install opencv-python mediapipe pyautogui dlib
```

> Some systems may require `cmake` or additional packages to build `dlib`.

---

## 🎯 Use Cases

* Accessibility tools for people with limited mobility
* Touchless interfaces for medical/cleanroom environments
* Smart desktops, HCI experiments, and educational demos
* Adding automatic screen lock for enhanced privacy and security

---

## 📌 Folder Structure

```
Computer-Vision-Projects/
├── Gesture-Controlled-Mouse/
├── Gaze-Controlled-Mouse/
├── Multi-Modal-Mouse/
├── AirWritingRecognizer/
├── Auto-Screen-Lock/
└── README.md  ← You're here!
```
---

## 🙌 Contributions

Pull requests and feedback are welcome.  
Feel free to explore, improve, or build upon any of these modules.

---

🚀 Empowering interaction through vision — touchless, intuitive, and human-centered.
