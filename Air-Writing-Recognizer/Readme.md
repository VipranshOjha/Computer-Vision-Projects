# ✍️ AirWritingRecognizer

**AirWritingRecognizer** is a real-time gesture-based system that allows users to draw letters in the air using only hand movements. It uses [MediaPipe](https://google.github.io/mediapipe/) for hand tracking and custom template matching to recognize handwritten uppercase English alphabets (A–Z).

---

## 🎯 Features

- ✋ Real-time hand tracking using webcam
- 🧠 Custom gesture control:
  - **Start Writing**: Touch **index finger** to **thumb**
  - **Stop & Recognize**: Touch **middle finger** to **thumb**
- 🔤 Recognizes characters based on finger trajectory
- 💡 Displays recognized text live on screen
- 📦 Self-contained: No deep learning model required

---

## 🛠️ Installation

1. Clone the repository:
   
   ```
   git clone https://github.com/VipranshOjha/Computer-Vision-Projects.git
   cd Computer-Vision-Projects/AirWritingRecognizer
   ```

2. Create a virtual environment (optional but recommended):

   ```
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows   
   ```

3. Install dependencies:

   ```
   pip install -r requirements.txt
   
   ```

---

## 🚀 Usage

Simply run the program:

```
python air_writing.py

```

* Make the **index-thumb gesture** to start drawing a letter.
* Use the **middle-thumb gesture** to stop and recognize the letter.
* The recognized characters will appear at the top of the window.

Press `Q` to quit.

---

## 🧠 How it Works

* Hand landmarks are tracked using MediaPipe.
* When in "writing mode", the fingertip trajectory is recorded.
* The recorded path is normalized and compared to predefined letter templates.
* Template matching is done by resampling the stroke and minimizing Euclidean distance.

---

## 📘 Future Improvements

* Add support for digits and lowercase letters
* Improve gesture smoothness using filters
* Integrate a neural network for more flexible handwriting recognition
* Add gesture for deleting, spacing, or confirming words

---

## 🙌 Acknowledgements

* [MediaPipe](https://google.github.io/mediapipe/) by Google for powerful hand tracking
* [OpenCV](https://opencv.org/) for real-time computer vision utilities

---

