import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(1)

mpHands = mp.solutions.hands
hands = mpHands.Hands()

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.Color_BGR2RGB)
    results = hands.process(imgRGB)
    print(results)

    cv2.imshow("Image", img)
    cv2.waitKey(1)