# 👁️ Gaze-Controlled Mouse

This project enables hands-free mouse control using real-time **eye tracking** through a webcam. It detects the user’s gaze to move the cursor and blinks to perform click actions.  
Ideal for **accessibility applications**, **hands-free interaction**, or experimentation in computer vision.

---

## 🚀 Features

- 👁️ **Gaze Tracking**: Moves the cursor based on pupil position.
- 👋 **Blink Detection**: Recognizes intentional blinks as click actions.
- ⚡ **Real-time Performance**: Uses efficient processing with `OpenCV` and `dlib`.

---

## 🧰 Dependencies

Install the required Python packages using:

```
pip install opencv-python dlib pyautogui

````

You may also need to install `cmake` and `dlib`'s build tools depending on your OS. For example on Ubuntu:

```
sudo apt-get install cmake
pip install dlib
```

---

## ▶️ How to Run

Make sure your webcam is connected, then run:

```
python EyeControlledMouse.py

```

---

## 🖱️ Controls

| Action            | Description                             |
| ----------------- | --------------------------------------- |
| Move Eyes         | Cursor moves with your gaze             |
| Blink (left eye)  | Performs a left-click action            |
| Blink (right eye) | Can be mapped to right-click            |

> ⚠️ Keep your face within the webcam’s view and ensure good lighting for best results.

---

## ⚙️ Customization

* **Sensitivity**: You can fine-tune sensitivity in the code by adjusting mapping of eye landmarks to screen coordinates.
* **Click Threshold**: Blink detection threshold can be adjusted for responsiveness.

---

## 📌 Use Cases

* Accessibility tools for individuals with limited mobility
* Hands-free UI for smart environments
* Experimental HCI (Human-Computer Interaction) projects

---

## 🙌 Contributions

Feel free to fork, modify, and improve this project.
Pull requests are welcome!

---
