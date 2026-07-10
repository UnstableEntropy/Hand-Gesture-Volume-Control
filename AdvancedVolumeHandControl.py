import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math
from pycaw.pycaw import AudioUtilities

#####--PARAMETERS--#####
wCam, hCam = 640, 480
############################

cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)
pTime = 0
cTime = 0

detector = htm.handDetector(detectionCon=0.7,maxHands=1)


device = AudioUtilities.GetSpeakers()
volume = device.EndpointVolume
# print(f"Audio output: {device.FriendlyName}")
# print(f"- Muted: {bool(volume.GetMute())}")
# print(f"- Volume level: {volume.GetMasterVolumeLevel()} dB")
volRange = volume.GetVolumeRange()
minVol = volRange[0]
maxVol = volRange[1]
vol = 0
volBar = 400
volPer = 0
area = 0
colorVol = (255,0,0)

while True:
    success,img = cap.read()

    #Find Hand
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img, draw=True)
    if len(lmList)!=0:

        #Filter Based on size
        area = (bbox[2]-bbox[0])*(bbox[3]-bbox[1])//100  #area = width * height
        if 200<area<1100:
            print("yes")
            #Find distance between index and thumb
            length, img, lineInfo = detector.findDistance(4,8,img) # 4-->Thumb ; 8-->Index

            #Convert volume
            volBar = np.interp(length, [50, 200], [400, 150])
            volPer = np.interp(length, [50, 200], [0, 100])

            #Reduce resolution to make it smoother
            smoothness = 5
            volPer = smoothness * round(volPer/smoothness)

            #Check fingers up
            fingers = detector.fingersUp()
            print(fingers)

            #If pinky is down then set volume
            if fingers[4]==False:
                volume.SetMasterVolumeLevelScalar(volPer/100,None)
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 10,
                            (0, 255, 0), cv2.FILLED)
                colorVol = (0,255,0)
            else:
                colorVol = (255,0,0)

    #Drawings
    cv2.rectangle(img, (50, 150), (87, 400), (255, 0, 0), 3)
    cv2.rectangle(img, (50, int(volBar)), (87, 400), (255, 0, 0), cv2.FILLED)
    cv2.putText(img, f'{int(volPer)}%', (40, 450), cv2.FONT_HERSHEY_COMPLEX,
                1, (255,0,0), 3)
    cVol = int(volume.GetMasterVolumeLevelScalar()*100)
    cv2.putText(img, f'Volume Set:{int(cVol)}', (400, 50),
                cv2.FONT_HERSHEY_COMPLEX, 1, colorVol, 3)


    #Frame Rate
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS:{int(fps)}', (40, 50),
                cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)


    cv2.imshow("Img", img)
    if cv2.waitKey(1) == ord('q'):
        break


