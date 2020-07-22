
import cv2
import numpy as np
import time
from PIL import Image, ImageGrab


# Clicking border 
clickBorder = [2,294,519,457]

im2 = ImageGrab.grab(bbox = clickBorder)
im2.show()

image = cv2.imread(im2)
gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
screen = np.array(im2)
cv2.imshow("Gray image", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()



print(screen[:3])
#im2.show()

#time.sleep(5)
#cv2.destroyAllWindows()

#screen = np.array(ImageGrab.grab(bbox=clickBorder))
#screen = cv2.cvtColor(screen, cv2.COLOR_RGB2GRAY)





