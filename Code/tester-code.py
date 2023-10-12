from time import sleep
from picozero import RGBLED

#RBG
rgb = RGBLED(red = 1, green = 2, blue = 3)

while True:
    rgb.color = (255, 0, 0) #red
    sleep(0.5)
    rgb.color = (0, 255, 0) #green
    sleep(0.5)
    rgb.color = (0, 0, 255) #blue
    sleep(0.5)
    rgb.color = (0, 255, 255) #cyan
    sleep(0.5)
    rgb.color = (255, 0, 255) #magenta
    sleep(0.5)
    rgb.color = (255, 255, 0) #yellow
    sleep(0.5)
    
