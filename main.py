import cv2
import numpy as np
import time
from PIL import Image, ImageGrab
import pyautogui


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
                



while True:

    startTime = time.time()
    image = np.array(ImageGrab.grab(bbox=clickBorder))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #image4 = Image.fromarray(image)
    #image4.show()
    shoot(image)
    print("Frame took {} seconds".format((time.time()-startTime)))

