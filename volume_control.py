import cv2
import numpy as np
import time
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from hand_tracker import HandDetector

# Volume Control Setup
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volRange = volume.GetVolumeRange()  # (min, max, step)
minVol, maxVol = volRange[0], volRange[1]

# Webcam Setup
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Width
cap.set(4, 480)  # Height

pTime = 0
detector = HandDetector(detectionCon=0.75)

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=True)

    if len(lmList) != 0:
        x1, y1 = lmList[4][1], lmList[4][2]   # Thumb tip
        x2, y2 = lmList[8][1], lmList[8][2]   # Index tip

        # Center point between fingers
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        # Draw line and circles
        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.circle(img, (cx, cy), 10, (0, 0, 255), cv2.FILLED)

        # Distance
        length = math.hypot(x2 - x1, y2 - y1)

        # Convert to volume
        vol = np.interp(length, [30, 200], [minVol, maxVol])
        volBar = np.interp(length, [30, 200], [400, 150])
        volPer = np.interp(length, [30, 200], [0, 100])
        volume.SetMasterVolumeLevel(vol, None)

        # Volume bar
        cv2.rectangle(img, (50, 150), (85, 400), (0, 0, 255), 2)
        cv2.rectangle(img, (50, int(volBar)), (85, 400), (0, 0, 255), cv2.FILLED)
        cv2.putText(img, f'{int(volPer)} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX,
                    1, (255, 0, 0), 2)

    # FPS Display
    cTime = time.time()
    fps = 1 / (cTime - pTime + 1e-5)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (10, 40),
                cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Hand Volume Control", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
