from ultralytics import YOLO
import cv2
import time
import os
from draw_rectangule import *

def dots_dots(n):
    
    if n==1:
        os.system("cls")
        print(BLUE+"running.".upper())
    
    else :
        if n==2:
            os.system("cls")
            print(BLUE+"running..".upper())
    
        else:
            if n==3:
                os.system("cls")
                print(BLUE+"running...".upper())

def n_seconds_video_record():

    # ---------------------------------------------------------
    # -----------------------SETTINGS--------------------------
    # load video
    print(PURPLE+ "introduce video path: ".upper())   
    video_path=input()

    # set video seconds
    print(PURPLE+ "provide seconds: ".upper())
    seconds= (int)(input())

    print(PURPLE+ "provide model path: ".upper())
    model_path=input()

    #catch video
    cap = cv2.VideoCapture(video_path)

    # ---------------------------------------------------------
    # --------------OUTPUT-VIDEO-SPECIFICATIONS----------------
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    out = cv2.VideoWriter('target.mp4',cv2.VideoWriter_fourcc('M','P','P','G'), 25, (frame_width,frame_height))

    # ---------------------------------------------------------
    # -------------------MAIN-LOOP-----------------------------
    
    # read frames
    start=time.time()
    
    num_frames=0
    success=True
    
    while True and success:

        dots_dots(1)
        
        success, frame = cap.read()

        num_frames+=1

        dots_dots(2)
        
        if time.time()-start>=seconds:        
            break
        
        #write in output video
        out.write(frame)
        
        dots_dots(3)

    cv2.destroyAllWindows()
    
    #clear console
    os.system("cls")

    return num_frames,model_path
    # ---------------------------------------------------------