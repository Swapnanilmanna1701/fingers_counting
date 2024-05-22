import cv2
import cvlearn.HandTrackingModule as htm
import cvlearn.FingerCounter as ctr
#this is for initiating webcam when 1= external webcam when 0=internal webcam
cap = cv2.VideoCapture(0)
detector = htm.handDetector()
fingers = ctr.FingerCounter()
while True:
    ret, frame = cap.read() #this is for read all the frame of video capture
    detector.findHands(frame)
    lmList, bbox = detector.findPosition(frame)
    if lmList != 0:
        fingers.drawCountedFingers(frame, lmList, bbox)
    cv2.imshow('result', frame) #this is for display the frame
    cv2.waitKey(1)
    