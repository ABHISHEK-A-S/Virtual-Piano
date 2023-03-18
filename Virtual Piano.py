import cv2
from cvzone.HandTrackingModule import HandDetector
from time import sleep
import cvzone
import math
from time import sleep
import pyglet



cap = cv2.VideoCapture(1,cv2.CAP_DSHOW)
cap.set(3, 1280)
cap.set(4, 720)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
cap.set(cv2.CAP_PROP_FPS, 60)
detector =HandDetector(maxHands=1,detectionCon=0.8)

while True:
    success, img = cap.read()
    #img = cv2.flip(img,1)
    hands,img = detector.findHands(img)


    #lmList, bboxInfo = detector.findPosition(img)
    for i in range(200,900,100):
        cv2.rectangle(img, (i, 600), (100, 300), (255, 255, 255),10)

    #for i in range(200, 900, 100):
    cv2.rectangle(img, (250, 300), (150, 100), (0, 0, 0), 10)
    cv2.rectangle(img, (350, 300), (250, 100), (0, 0, 0), 10)

    for i in range(550, 850, 100):
        cv2.rectangle(img, (i, 300), (i-100, 100), (0, 0, 0), 10)

    if hands:
        # Hand 1
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # List of 21 Landmarks points
        bbox1 = hand1["bbox"]  # Bounding Box info x,y,w,h
        centerPoint1 = hand1["center"]  # center of the hand cx,cy
        handType1 = hand1["type"]  # Hand Type Left or Right
        x1=lmList1[8][0]
        y1 = lmList1[8][1]
        x2 = lmList1[4][0]
        y2 = lmList1[4][1]
        dist=math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2))



        if 100<x1<200 and 300<y1<600 and dist<35:
            cv2.rectangle(img, (200, 600), (100, 300), (0, 255, 0), 7)
            playsound("c1.wav")
            sleep(0.15)

        if 200 < x1 < 300 and 300 < y1 < 600 and dist < 35:
            cv2.rectangle(img, (300, 600), (200, 300), (0, 255, 0), 7)
            playsound("d1.wav")
            sleep(1)

        if 300 < x1 < 400 and 300 < y1 < 600 and dist < 35:
            cv2.rectangle(img, (400, 600), (300, 300), (0, 255, 0), 7)
            playsound("e1.wav")
            sleep(1)

        if 400 < x1 < 500 and 300 < y1 < 600 and dist < 35:
            cv2.rectangle(img, (500, 600), (400, 300), (0, 255, 0), 7)
            playsound("f1.wav")
            sleep(1)




        for i in range(150,350,100):
            if i<x1<i+100 and 100<y1<300 and dist<35:
                    cv2.rectangle(img, (i+100, 300), (i, 100), (0, 255, 0), 7)
        for i in range(450,750,100):
            if i<x1<i+100 and 100<y1<300 and dist<35:
                    cv2.rectangle(img, (i+100, 300), (i, 100), (0, 255, 0), 7)


    #cv2.rectangle(img, (200,400), (100,100), (255, 255, 255),cv2.FILLED )
    #cv2.putText(img[1], "P", (60, 430),cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 5)
   # cv2.rectangle(img, (500, 100), (6, 5), (255, 255, 255), cv2.FILLED)

    #img = cv2.flip(img[1], 1)
    cv2.imshow("Image",img)
    cv2.waitKey(1)