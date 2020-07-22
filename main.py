import time
import cv2
import numpy as np
from PIL import Image, ImageGrab
import pyautogui

clickBorder = [2, 294, 519, 457]

def shoot_fnct(screen):
    global clickBorder

    for y in range(len(screen)):
        for x in range(len(screen[y])):
            if screen[y][x] < 10:
                actual_x = x + clickBorder[0]
                actual_y = y + clickBorder[1]
                pyautogui.click(actual_x, actual_y, clicks=1)





#takes screenshot of the clickborder, then converts it to a numpy array.
while True:
    
    startTime = time.time()
    screen = np.array(ImageGrab.grab(bbox=clickBorder))
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

    print(screen)
