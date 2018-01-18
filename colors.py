import numpy as np
import cv2

width = 712
height = 712

img =  np.zeros((height,width,3), np.uint8)


def drawPixel():
    cv2.rectangle(img, (100 + 2 * x, 100 + 2 * y), (100 + 2 * x + 1, 100 + 2 * y + 1), color)

for i in range(256):
    for j in range(256):
        x = i
        y = j
        red = x
        green = 0
        blue = y
        color = (red, green , blue)
        if (int(i / 4) + int(j / 4)) % 2 == 0:
            drawPixel()


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
