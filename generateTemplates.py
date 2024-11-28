import os
import cv2
import mediapipe as mp

mp_drawing=mp.solutions.drawing_utils
mp_pose=mp.solutions.pose


pose=mp_pose.Pose(
    min_detection_confidence=0.6,
    min_tracking_confidence=0.5
)

def StartTest(directory):
    f=open("TemplatesDollar.py","a")
    recstring=""
    for file_name in os.listdir(directory):
        if file_name.endswith(".mp4"):
            f.write("\nresult=recognizer.recognize([")
            print(file_name)
            cap=cv2.VideoCapture(directory+"/"+file_name)
            framcnt=0

            while cap.isOpened():
                ret,frame=cap.read()
                if not ret:
                    print("no frame received")
                    break
                frame=cv2.resize(frame,(640,480))
                framcnt+=1
                try:
                    RGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                    print(framcnt)
                    result=pose.process(RGB) 

                    image_height,image_width,_ =frame.shape
                    x=str(int(result.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].x*image_width))
                    y=str(int(result.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].y*image_height))
                    f.write("point("+x+","+y+",1),\n")

                    x=str(int(result.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].x*image_width))
                    y=str(int(result.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].y*image_height))
                    f.write("point("+x+","+y+",1),\n")
                    
                    mp_drawing.draw_landmarks(frame,result.pose_landmarks,mp_pose.POSE_CONNECTIONS)
                    cv2.imshow('output',frame)

                except:
                    break
                if cv2.waitKey(1)==ord('q'):
                    break
            f.write("])\n")
            f.write("print(result)\n")
            cap.release()
            cv2.destroyAllWindows()
    f.close()


def loop_files(directory):
    f=open("test3dollar.py","w")
    f.write("from dollarpy import Recognizer,Template,Point\n")
    recstring=""
    for file_name in os.listdir(directory):
        if os.path.isfile(os.path.join(directory,file_name)):
            if file_name.endswith(".mp4"):
                print(file_name)
                foo=file_name[:-4]
                recstring+=foo+","
                f.write(""+foo+"= Template('"+foo+"',[\n")
                cap=cv2.VideoCapture(file_name)
                framecnt=0
                while cap.isOpened():
                    ret,frame=cap.read()
                    if not ret:
                        print("no frames recieved")
                        break
                    frame=cv2.resize(frame,(480,320))
                    framecnt+=1
                    try:
                        RGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                        print(framecnt)
                        results=pose.process(RGB)
                        image_height,image_width,_=frame.shape

                        image_height,image_width,_ =frame.shape
                        for i in range(32):
                            x=str(int(result.pose_landmarks.landmark[i].x*image_width))
                            y=str(int(result.pose_landmarks.landmark[i].y*image_height))
                            f.write("point("+x+","+y+",1),\n")
                        mp_drawing.draw_landmarks(frame,results.pose_landmarks,mp_pose.POSE_CONNECTIONS)
                        cv2.imshow('output',frame)

                    except:
                        break
                    if cv2.waitKey(1)==ord('q'):
                        break
                f.write("])\n")
                cap.release()
                cv2.destroyAllWindows()
    recstring=recstring[:-1]
    f.write("recognizer=Recognizer(["+recstring+"])\n")
    f.close()
                       