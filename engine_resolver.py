from ultralytics import YOLO
import torch
import sys
from draw_rectangule import *
import os


# return a list of Results objects
def engine_resolver(model,image):
        
    results = model(image)

    # clean console after calculations
    os.system("cls")

    label=1
    target_list=[]

    #------------------------------------------------------------
    #------------EXTRACT-REACTANGULE-----------------------------
    for result in results:
        
        # Boxes object for box outputs           
        boxes = result.boxes  
        
        for i in boxes.xywh:
            
            # set a label
            label+=1
            text="object: "+ label.__str__()

            #-------CONVERTION-FROM-TENSOR-TO-LIST---------------
            xywh_tensor = torch.tensor(i)
                
            xywh_list = xywh_tensor.tolist()  # Convert tensor to a list
                
            x, y, width, height = xywh_list  # Access the individual elements

            #---------------------------------------------------
            # define start/end points
            x_start=x-width/2
            y_start=y+height/2
            
            x_end=x_start+ width
            y_end=y_start-height
            
            #---------------------------------------------------
            # add label and points to list for drawing
            target_list.append((text,x_start,y_start,x_end,y_end))    
    
    #-----------------------------------------------------------
    #------DRAW-RECTANGULE--------------------------------------
    
    image = draw_rectanguleFunc(image,target_list)        
        
    #-----------------------------------------------------------
    
    return image
        