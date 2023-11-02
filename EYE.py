import cv2
import numpy as np
from draw_rectangule import *
from ultralytics import YOLO
from engine_resolver import engine_resolver
import os
from video_target_get import n_seconds_video_record
import time

all_times=[]

def status(state,num_frames,actual_frame,start_timer):
  
  # clean console
  os.system("cls")

  if state<0.5:
          
          print(RED+ f"there are {num_frames-actual_frame} frame left".upper())
          
  else :
          
    if state>=0.5 and state<0.8:
          
      print(YELLOW+ f"there are {num_frames-actual_frame} frame left".upper())

    else :
          
      if state>=0.8 and state<0.95:
          
        print(GREEN+ f"there are {num_frames-actual_frame} frame left".upper())

      else :
              
        if state>=0.95:             
          
          print(CYAN+ f"there are {num_frames-actual_frame} frame left".upper())
  
  # ---------------------------------------------
  # --------------------SHOW-STATUS-BAR----------
  status_bar="|"
  
  length=int(state * 100)
  
  for i in range(length):
    status_bar+=GREEN+ "-"

  for i in range(100-length):
    status_bar+=RED+ "-"

  status_bar+="|"


  all_times.append(time.time()-start_timer)
  all_times_sum=0

  for i in all_times:
    all_times_sum+=i  
  
  print(GREEN + status_bar+GREEN +f" {length}% {all_times.__len__()/all_times_sum} FRAMES/s ")
# -----------------------------------------------------------------------------


def main_loop(num_frames):

  # ---------------------------------------------------------
  # --------------LOAD-TARGET--------------------------------

  # Create a VideoCapture object
  cap = cv2.VideoCapture('target.mp4')

  # Check if camera opened successfully
  if (cap.isOpened() == False): 
    print(RED+"Unable to read camera feed".upper())
  
  # ---------------------------------------------------------
  # --------------OUTPUT-VIDEO-SPECIFICATIONS----------------

  # Default resolutions of the frame are obtained.The default resolutions are system dependent.
  # We convert the resolutions from float to integer.
  frame_width = int(cap.get(3))
  frame_height = int(cap.get(4))

  # Define the codec and create VideoWriter object.
  # specify the output format and number of frames.
  out = cv2.VideoWriter('outpy.mp4',cv2.VideoWriter_fourcc('M','P','P','G'), 25, (frame_width,frame_height))

  # ---------------------------------------------------------
  # --------------------LOAD-MODEL---------------------------
  # Load a model
  print(YELLOW+"loading model...".upper())

  model = YOLO('A:\\COLLEGE\\Computing_Science\\3rd year\\Segundo semestre\\Computation View\\OptativoCV\\ModelsWeights\\YOLOv8\\yolov8x.pt')  # pretrained YOLOv8n model

  print(GREEN+"model loaded.".upper())

  # ---------------------------------------------------------
  # -------------------------MAIN-LOOP-----------------------
  
  actual_frame=0

  while(True):

    # start timer for frame processing
    start_timer=time.time()    

    ret, frame = cap.read()
  
    actual_frame+=1

    if ret == True: 
      
      # -------------------------------------------------------
      # --------------------CONVERTION-------------------------
      # convert image to RGB
      frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

      # convert from array to image
      frame= Image.fromarray(frame)
      
      #-----------------------------------------------------------
      #-------------------ENGINE----------------------------------
      
      frame= engine_resolver(model,frame)
        
      # -------------------------------------------------------
      # --------------------CONVERTION-------------------------
      
      # convert back image to numpy array
      frame= np.array(frame)    
      # convert image to RGB
      frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

      # --------------------------------------------------------
      # --------------------STORAGE-----------------------------
      
      # Write the frame into the file 'outpy.mp4'            
      out.write( frame)

      # --------------------------------------------------------
    
      status(actual_frame/num_frames,num_frames,actual_frame,start_timer)

    else: 
      break
  # -----------------------------------------------------------
  # --------------RELEASE-RESOURCES----------------------------
  
  # When everything done, release the video capture and video write objects
  cap.release()
  out.release()

  # Closes all the frames
  cv2.destroyAllWindows()
  # --------------------------------------------------------


# build n-second video
num_frames= n_seconds_video_record()

# start program
main_loop(num_frames)

# clean console
os.system("cls")

# delete video target 
os.remove("target.mp4")

# A:\story of mine\uni\20211103_084128.mp4