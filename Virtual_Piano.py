
import cv2 
import winsound 
import numpy as np 

FREQUENCIES = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88, 523.25]

def play_note(i):
    if 0 <= i < len(FREQUENCIES):
        freq = FREQUENCIES[i]
        winsound.Beep(int(freq), 500)

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Cannot open webcam.")
    exit(1)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
last_key = -1

print("Motion piano: move your hand in top strip to play notes.")

while True:
    ret, frame = cap.read()
    if not ret: break

    current_key = -1
    frame = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_skin = np.array([0, 40, 60])
    upper_skin = np.array([20, 255, 255])
    mask = cv2.inRange(hsv, lower_skin, upper_skin)

    roi = mask[:60, :]
    contours, _ = cv2.findContours(roi, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    current_key = -1
    if contours:
        cnt = max(contours, key=cv2.contourArea)
        M = cv2.moments(cnt)
        if M["m00"] > 0:
            x = int(M["m10"] / M["m00"])
            key_width = width // len(FREQUENCIES)
            current_key = min(len(FREQUENCIES) - 1, max(0, x // key_width))

    key_width = width // len(FREQUENCIES)

    for i in range(len(FREQUENCIES)):
        color = (100, 100, 100)
        if i == last_key: 
            color = (0, 255, 0)
        x1 = i * key_width
        x2 = (i + 1) * key_width
        cv2.rectangle(frame, (x1, 0), (x2, 60), color, -1)
        cv2.putText(frame, f"{['C','D','E','F','G','A','B','C'][i]}", (x1 + 10, 40), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 255, 255), 1)

    if current_key != last_key and current_key >= 0:
        play_note(current_key)
        last_key = current_key

    cv2.imshow("Invisible Piano", frame)
    if cv2.waitKey(1) & 0xFF == 27: break

cap.release()
cv2.destroyAllWindows()
