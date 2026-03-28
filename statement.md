## Project Documentation : *Computer Vision Virtual Piano*

# Problem Statement
Traditional musical instruments require physical interaction, which can be a barrier for users with limited mobility or those seeking an experimental, touchless interface. Furthermore, creating interactive multimedia applications often involves expensive sensors or complex hardware.

The goal of this project is to develop an "Invisible Piano" that uses Real-Time Image Processing to detect human motion within specific regions of a video feed. By mapping the horizontal position of a user’s hand to specific musical frequencies, the system creates a low-cost, accessible, and interactive digital instrument using only a standard webcam and Python-based computer vision techniques.

# Key Challenges Addressed

* Motion Segmentation: Distinguishing the user's hand from the background using HSV skin-tone filtering.
* Dynamic Mapping: Dividing the camera's field of view into discrete "virtual keys" that correspond to the musical C-major scale.
* Latency Management: Ensuring the audio output (via winsound) triggers immediately upon motion detection for a seamless user experience.

# **Scope of the Project**

The current project establishes a Minimum Viable Product (MVP) by mapping 2D coordinates to simple frequencies. The scope can be categorized into three developmental phases:

***1. Current Functional Scope***

* Real-time Hand Tracking: Detection of skin-tone centroids within a defined Region of Interest (ROI).
* Virtual Mapping: Dividing the video frame into 8 discrete "trigger zones" representing a C-major scale.
* Visual Feedback: On-screen GUI showing active "keys" and note labels (C, D, E, F, G, A, B, C).

***2. Technical Enhancements (Potential)***

* Polyphony: Upgrading the audio engine from winsound (which is monophonic and blocking) to pygame.mixer to allow playing multiple notes or chords simultaneously.
* Advanced Tracking: Replacing basic HSV color filtering with MediaPipe Hands to track specific fingertips rather than just a general "blob" of skin.
* Instrument Synthesis: Implementing MIDI output so the software can control professional digital audio workstations (DAWs) like Ableton or FL Studio.

***3. Environmental Adaptability***

Dynamic Calibration: Adding a feature to calibrate the background or lighting conditions to reduce "noise" in the motion detection.



# **Target Users**

The project appeals to a diverse group of users, ranging from hobbyists to specialists:



|***USER CATEGORY***|***USE CASE***|
|-|-|
|Students \& Educators|As a STEM learning tool to demonstrate the intersection of Physics (Sound), Math (Coordinates), and Computer Science.|
|People with Disabilities|As an Assistive Technology for individuals with limited fine motor skills who cannot press physical keys but can move their arms in space.|
|Interactive Exhibit Designers|For museums or art installations where a "touchless" interface is required for hygiene or novelty.|
|Beginner Programmers|As a gateway project into OpenCV and real-time data processing.<br />	|
|Experimental Musicians|Using the interface as a "Theremin-style" controller to create unique, gestural performances.|



Thank You.	               

&#x09;       



