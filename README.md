🎛️# Hand Based Computer Volume Control 
A Python-based application that enables users to control their system's volume using hand gestures captured via a webcam. By leveraging computer vision techniques, the application detects the distance between the thumb and index finger to adjust the volume level in real-time.​

📌 Features
Real-time hand tracking using webcam input​

Gesture recognition to control system volume​

Visual feedback displaying volume level​

Cross-platform compatibility (Windows, macOS, Linux)​

🛠️ Installation
Clone the repository:
git clone https://github.com/PataskarSharvari/HandGestureVolumeControl.git
cd HandGestureVolumeControl
Create and activate a virtual environment (optional but recommended):
bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate


🚀 Usage
Run the application:
python volume_control.py

Instructions:
Ensure your webcam is connected and functioning.​
Place your hand in front of the webcam.​
Adjust the distance between your thumb and index finger to increase or decrease the volume.​
The application will display the current volume level on the screen.​

📂 Project Structure

HandGestureVolumeControl/
├── hand_tracker.py       # Module for hand detection and tracking
├── volume_control.py     # Main application script
├── requirements.txt      # List of required Python packages
├── README.md             # Project documentation


✅ Dependencies
Python 3.x​
OpenCV​
MediaPipe​
GitHub Docs
NumPy​
pycaw (for Windows systems)​


🤝 Contributing
Contributions are welcome! If you have suggestions for improvements or encounter any issues, feel free to open an issue or submit a pull request.​

📄 License
This project is licensed under the MIT License.​

🙋‍♀️ Author
Developed by Sharvari Pataskar.
