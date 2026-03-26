# Virtual-piano
A Python-based computer vision application that transforms your webcam into an invisible musical instrument. By detecting hand movements within a specific "hot zone" at the top of the screen, the program triggers musical notes (C Major scale) using real-time image processing.

#  How It Works:
The application uses OpenCV to process video frames and Windows Sound API (winsound) to generate audio.
- Skin Detection: The script converts the BGR video feed to HSV (Hue, Saturation, Value) color space to isolate skin tones using a predefined range.
- Region of Interest (ROI): It specifically monitors a 60-pixel tall strip at the top of the webcam feed.
- Contour Tracking: The program finds the largest object (your hand) within that strip and calculates its center point ($x, y$ moments).
- Note Mapping: The screen width is divided into 8 segments corresponding to the notes: C, D, E, F, G, A, B, C.
- Trigger Logic: When your hand enters a new segment, the winsound.Beep function triggers the corresponding frequency.
# 🚀 Getting Started 
- Prerequisites
- - OS: Windows (Required for the winsound library).
  - Hardware: A functional webcam.
  - Python: 3.x
- Installation
- - Clone the repository: git clone https://github.com/yourusername/virtual-piano.git
cd virtual-piano
Install dependencies:Bashpip install opencv-python numpy
🎮 UsageRun the script:Bashpython Virtual_Instrument.py
Position yourself so your hand is visible to the webcam.Move your hand horizontally across the top strip of the window.The keys will turn green when triggered.Press ESC to exit the application.🛠️ Technical DetailsColor Masking: Uses cv2.inRange with HSV values:Lower: [0, 40, 60]Upper: [20, 255, 255]Frequency Logic: The notes are mapped to standard scientific pitch frequencies:| Note | Frequency (Hz) || :--- | :--- || C4   | 261.63 || A4   | 440.00 || C5   | 523.25 |📝 TroubleshootingLighting: Ensure you are in a well-lit area. Skin detection is sensitive to shadows and extreme yellow/red lighting.Background: Try to have a neutral background; objects with colors similar to skin tones may cause "ghost notes."
