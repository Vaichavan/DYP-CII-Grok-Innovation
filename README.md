# DYP-CII-Grok-Innovation


## 📂 Project Structure

This repository is organized into three main components:

### 1. 🔡 Allkeyboard_pycharm

A keyboard-based automation system built with OpenCV and CVZone.

- `main.py` – Primary script for handling camera input and automation logic  
- `rule.py` – Defines operational or automation rules  
- `/cvzone/` – Utility modules for simplified computer vision tasks  
  - Includes submodules such as `FaceDetectionModule`, `HandTrackingModule`, `SelfieSegmentationModule`, and others

### 2. 🔐 Safe_door

Microcontroller-integrated scripts powering a secure door prototype.

- `1robotmobile.py` – Code for mobile robot behavior  
- `2robotcp.py` – Handles control panel or communication protocol  
- `alaram.py` – Alarm/alert system integration  
- `code.py` – Manages door logic and sensor inputs

### 3. 📘 Guide_pdf

Documentation, setup instructions, and user guides for the system.

---

## 🚀 Features

- ✅ Real-time hand, face, and pose tracking with **CVZone**  
- ✅ Automated keyboard actions triggered via camera input  
- ✅ Robotics-based secure door prototype with motion detection and alarm capabilities  
- ✅ Modular, reusable Python code architecture  
- ✅ Built on Python 3 with OpenCV integration

---

## ⚙️ Requirements

Install the required dependencies using pip:

```bash
pip install opencv-python cvzone numpy

-------


🧪 How to Run
🖥️ Allkeyboard (Computer Vision Automation)
bash
Copy
Edit
cd Allkeyboard_pycharm
python main.py
🔐 Safe Door Robot System
bash
Copy
Edit
cd Safe_door
python 1robotmobile.py
You can also run other modules depending on your configuration:

2robotcp.py – for the control panel interface

alaram.py – for alarm or alert triggers

📎 Notes
Ensure your camera is connected and accessible via OpenCV.

Some modules require additional hardware (such as a Raspberry Pi, sensors, or motors).

Refer to the Guide_pdf folder for detailed setup and usage instructions.

📌 License
This project is intended exclusively for academic, research, and innovation showcase purposes under the DYP-CII Grok Innovation framework.

🙏 Acknowledgements
Developed using CVZone by Murtaza Hassan

Inspired by real-world robotics and smart security applications

Created by: Vaichavan


