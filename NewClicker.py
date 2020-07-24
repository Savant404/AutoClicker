import cv2
import numpy as np
import time
from PIL import Image, ImageGrab
import pyautogui


# Clicking border 
clickBorder = [19,545,724,697]



def shoot(screen):
    global clickBorder

    for y in range(5,len(screen)-5):
        for x in range(5,len(screen[y])-5):
            if screen[y][x] < 10:
                click_x = x + clickBorder[0]
                click_y = y + clickBorder[1] 
                print(click_x, click_y)
                pyautogui.click(click_x, click_y)
                pyautogui.click(click_x, click_y)
                return
                


im2 = ImageGrab.grab(bbox = clickBorder)
#im2.show()

image = np.array(im2, dtype=np.uint8)
image2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image3 = Image.fromarray(image2)
image3.show()




    
     


#pixels = [list(i) for i in image2]
    

#print(image2[0:179])
#print(pixels[0:3])
#print(pixels)

#print(len(pixels))
#print(len(pixels[:1]))

 
      
 
        
            

