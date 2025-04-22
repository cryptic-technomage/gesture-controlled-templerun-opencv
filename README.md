# 🏃‍♂️ Temple Run Gesture Controller using OpenCV & MediaPipe

Control **Temple Run** with just your **hand gestures** — no mouse, no keyboard!  
This project brings computer vision and automation together to create an immersive, hands-free gaming experience using **Python**, **OpenCV**, **MediaPipe**, and the **keyboard** module.

![Gesture Controller Demo](demo.gif)  

---

## ✨ Features

- 🎮 **No Touch Controls** — Play Temple Run using only hand gestures.
- 🖐️ Real-time **gesture recognition** with OpenCV + MediaPipe.
- ⚡ Seamless **keyboard input automation** using `keyboard` library.
- 🧠 Simple, intuitive gestures:
  - **Raise left index finger** → Turn **Left**
  - **Raise right index finger** → Turn **Right**
  - **Raise index fingers of both hands** → **Slide Down**
  - **Raise all fingers on right hand** → **Jump**

---

## 🛠️ Tech Stack

- [Python](https://www.python.org/)
- [OpenCV](https://opencv.org/) – Real-time video processing
- [MediaPipe](https://ai.google.dev/edge/mediapipe/solutions/guide) – Hand tracking and gesture recognition
- [keyboard](https://pypi.org/project/keyboard/) – Simulate keypresses

---

## 📦 Installation

### 1. Clone this repository

```bash
git clone https://github.com/cryptic-technomage/gesture-controlled-templerun-opencv.git
cd gesture-controlled-templerun-opencv
```

### 2. Install dependencies
Make sure you're using Python 3.7 or higher.

```bash
pip install opencv-python mediapipe keyboard
```

### 3. Run the script

```bash
python temple_run_gesture_controller.py
```

## ✋ Gesture Controls

Keep your hands visible to the webcam. Optimal performance might depend on lighting conditions and background clutter.

| Gesture                       | Action      | Keyboard Input |
| :---------------------------- | :---------- | :------------- |
| Right hand — all fingers up   | Jump        | `up`           |
| Left hand — index finger up  | Turn Left   | `left`         |
| Right hand — index finger up | Turn Right  | `right`        |
| Both hands — index fingers up | Slide Down  | `down`         |

## 🙌 Credits

Built with ❤️ by Sandeep using Python, OpenCV, and MediaPipe.

## 📄 License
This project is licensed under the MIT License.



