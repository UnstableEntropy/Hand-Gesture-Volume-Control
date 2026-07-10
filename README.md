# 🎛️ Gesture-Controlled System Volume Controller

Control your computer's system volume using hand gestures in real time! This project uses **Computer Vision** and **MediaPipe** to detect hand landmarks through a webcam and adjust the system volume based on the distance between the thumb and index finger.

## 🚀 Features

- ✋ Real-time hand tracking using MediaPipe
- 🔊 Control system volume with thumb–index finger distance
- ✅ Pinky-finger confirmation gesture to prevent accidental volume changes
- 📊 Live volume percentage display
- 📦 Hand bounding box detection
- ⚡ FPS (Frames Per Second) display for performance monitoring

## 🛠️ Technologies Used

- Python
- OpenCV
- MediaPipe
- NumPy
- Pycaw (Windows Audio Control)

## 📂 Project Structure

```
Gesture-Controlled-Volume/
│
├── AdvancedVolumeHandControl.py    # Main application
├── HandTrackingModule.py           # Hand tracking utilities
└── README.md
```

## ⚙️ Installation

1. Clone the repository.

```bash
git clone https://github.com/<your-username>/Gesture-Controlled-Volume.git
cd Gesture-Controlled-Volume
```

2. Install the required libraries.

```bash
pip install opencv-python mediapipe numpy pycaw comtypes
```

3. Run the application.

```bash
python AdvancedVolumeHandControl.py
```

## 🎮 How It Works

1. The webcam captures live video.
2. MediaPipe detects and tracks hand landmarks.
3. The distance between the thumb and index finger is calculated.
4. This distance is mapped to the system volume.
5. Volume changes are applied only when the **pinky finger is folded**, reducing accidental adjustments.
6. The current volume level and FPS are displayed on the screen.

## 📸 Demo

Add screenshots or a GIF here.

Example:

```
demo.gif
```

## 🔮 Future Improvements

- Brightness control using gestures
- Gesture-controlled media player
- Customizable gesture mapping
- Multi-hand gesture support
- Cross-platform audio control

## 🙏 Acknowledgements

This project was developed by following the **Hand Tracking** and **Gesture Control** tutorials by **Murtaza's Workshop – Robotics and AI**. It was created as part of my learning journey in Computer Vision using OpenCV and MediaPipe.

## 📄 License

This repository is shared for educational purposes. Since it is based on a tutorial project, no license has been specified.

