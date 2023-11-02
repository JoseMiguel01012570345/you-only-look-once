import tkinter as tk
from PIL import Image, ImageTk ,ImageDraw
import cv2

#-----------------------------------------CONSOLE-COLORS--------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------

BLACK = '\033[0;30m'
RED = '\033[0;31m'
GREEN = '\033[0;32m'
YELLOW = '\033[0;33m'
BLUE = '\033[0;34m'
PURPLE = '\033[0;35m'
CYAN = '\033[0;36m'
WHITE = '\033[0;37m'
RESET = '\033[0m'

#---------------------------------------------------------------------------------------------------------------
#-------------------------------------------DRAWING-------------------------------------------------------------
def draw_rectanguleFunc(image,target_list):

    for target in target_list:
    
        try:
            # Create a draw object
            draw = ImageDraw.Draw(image)

            # Paint the rectangle on the image
            draw.rectangle([target[1],target[4], target[3], target[2]], outline="red", width=2)

            # draw thin ractangule above object and label
            draw.rectangle([target[1], target[4]-25,target[3],target[4]], outline="red", width=1)
            
            # add label
            draw.multiline_text([target[1]+20, target[4]-15,target[3],target[4]],target[0],fill='red' ,align="center")


        except Exception as e:
            # couldn't draw
            print(RED+ "there was an error: ".upper(),e)    
    
    # Display the image
    # image.show()
    
    return image
#-------------------------------------------------------------------------------------------------------------------
#-----------------------------------------BUILD_SCREEN_PHOTO--------------------------------------------------------
# Resize image to screen size
def create_img(image,img_newPath):

    root = tk.Tk()    

    # Get the screen width and height

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate the aspect ratio of the image

    image_width = image.shape[1]
    image_height = image.shape[0]
    aspect_ratio = image_width / image_height

    # Calculate the new width and height to fit the screen

    if aspect_ratio > screen_width / screen_height:
        
        new_width = screen_width
        new_height = int(screen_width / aspect_ratio)

    else:
        
        new_width = int(screen_height * aspect_ratio)
        new_height = screen_height

    # Resize the image
    image = cv2.resize(image, (new_width, new_height))

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Convert the numpy array to a PIL Image
    image = Image.fromarray(image)

    image.save(img_newPath)

    # Convert the PIL Image to a PhotoImage
    photo = ImageTk.PhotoImage(image)

    canvas = tk.Canvas(root, width=photo.width(), height=photo.height())
    canvas.pack()

    canvas.create_image(0, 0, image=photo, anchor="nw")

    return photo
# create_img caller using image path
def create_img_by_path(img_path,img_newPath):
    
    image = cv2.imread(img_path)    
    
    create_img(image,img_newPath)

    new_image= Image.open(img_newPath)

    new_image.show()   