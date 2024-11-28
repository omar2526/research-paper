import os
import cv2
import mediapipe as mp

mp_drawing=mp.solutions.drawing_utils
mp_pose=mp.solutions.pose


pose=mp_pose.Pose(
    min_detection_confidence=0.6,
    min_tracking_confidence=0.5
)

cap=cv2.VideoCapture(0)
framcnt=0

while cap.isOpened():
    ret,frame=cap.read()
    if not ret:
        print("no frame received")
        break
    frame=cv2.resize(frame,(640,480))
    framcnt+=1
    RGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    print(framcnt)
    result=pose.process(RGB) 

    mp_drawing.draw_landmarks(frame,result.pose_landmarks,mp_pose.POSE_CONNECTIONS)
    cv2.imshow('output',frame)

    if cv2.waitKey(1)==ord('q'):
        break

cap.release()