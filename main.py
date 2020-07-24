<<<<<<< HEAD
=======
import time
>>>>>>> 5f197fb926d102a3b18ab40273a913e7b968effb
import cv2
import numpy as np
from PIL import Image, ImageGrab
import pyautogui

clickBorder = [2, 294, 519, 457]

<<<<<<< HEAD
# Clicking border 
clickBorder = [19,545,724,697]



def shoot(image):
    global clickBorder

    for y in range(len(image)):
        for x in range(len(image[y])):
            if image[y][x] < 10:
                click_x = x + clickBorder[0]
                click_y = y + clickBorder[1] 
                print(click_x, click_y)
                pyautogui.click(click_x, click_y)
                mouse_x, mouse_y = pyautogui.position()
                print(mouse_x,mouse_y)
                
                return
                
=======
def shoot_fnct(screen):
    global clickBorder

    for y in range(len(screen)):
        for x in range(len(screen[y])):
            if screen[y][x] < 10:
                actual_x = x + clickBorder[0]
                actual_y = y + clickBorder[1]
                pyautogui.click(actual_x, actual_y, clicks=1)

>>>>>>> 5f197fb926d102a3b18ab40273a913e7b968effb



while True:

<<<<<<< HEAD
    startTime = time.time()
    image = np.array(ImageGrab.grab(bbox=clickBorder))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #image4 = Image.fromarray(image)
    #image4.show()
    shoot(image)
    print("Frame took {} seconds".format((time.time()-startTime)))
=======
#takes screenshot of the clickborder, then converts it to a numpy array.
while True:
    
    startTime = time.time()
    screen = np.array(ImageGrab.grab(bbox=clickBorder))
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
>>>>>>> 5f197fb926d102a3b18ab40273a913e7b968effb

    print(screen)
