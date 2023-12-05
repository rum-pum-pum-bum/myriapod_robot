from picozero import Motor
from time import sleep
from machine import Pin
from picozero import Speaker

#initializing motors for individual motor control
segment1left = Motor(2,3)
segment1right = Motor(4,5)
segment2left = Motor(6,7)
segment2right = Motor(8,9)
segment3left = Motor(10,11)
segment3right = Motor(12,13)

#turn on the light on the pi pico to show it is on
led = Pin(25, Pin.OUT)
led.toggle()

def move_forward():
    #function to be called to run motors at full speed forward
    #segment 1
    segment1left.backward()
    segment1right.forward()
    #segment 2
    segment2left.backward()
    segment2right.forward()
    #segment 3
    segment3left.backward()
    segment3right.forward()
    
def move_half_speed():
    #function to be called to put all motors at a slower speed
    #segment 1
    segment1left.backward(0.25)
    segment1right.forward(0.25)
    #segment 2
    segment2left.backward(0.25)
    segment2right.forward(0.25)
    #segment 3
    segment3left.backward(0.25)
    segment3right.forward(0.25)
    
def left_turn():
    #function to be called to make a left turn
    #segment 1
    segment1left.backward(0.25) #0.25 = 25% of the speed via PWM control
    segment1right.forward(0.75) #0.75 = 75% speed to put less strain on the curve
    #segment 2
    #add a slight delay if needed like when doing a corner in a parade with a marching band
    sleep(0.5)
    segment2left.backward(0.25)
    segment2right.forward(0.75)
    #segment 3
    #add a slight delay if needed like when doing a corner in a parade with a marching band
    sleep(0.5)
    segment3left.backward(0.25)
    segment3right.forward(0.75)

def right_turn():
    #function to be called to make a right turn
    #segment 1
    segment1left.backward(0.75) #0.75 = 75% speed to put less strain on the curve
    segment1right.forward(0.25) #0.25 = 25% of the speed via PWM control
    #segment 2
    #add a slight delay if needed like when doing a corner in a parade with a marching band
    sleep(0.5)
    segment2left.backward(0.75)
    segment2right.forward(0.25)
    #segment 3
    #add a slight delay if needed like when doing a corner in a parade with a marching band
    sleep(0.5)
    segment3left.backward(0.75)
    segment3right.forward(0.25)
    
def end_turn():
    #function to be called to end the turn sequence
    #segment 1
    #bring speeds to the same slower speed
    segment1left.backward(0.75)
    segment1right.forward(0.75)
    #segment 2
    #add a slight delay if needed like when doing a corner in a parade with a marching band
    sleep(0.5)
    segment2left.backward(0.75)
    segment2right.forward(0.75)
    #segment 3
    #add a slight delay if needed like when doing a corner in a parade with a marching band
    sleep(0.5)
    segment3left.forward(0.75)
    segment3right.forward(0.75)
    sleep(5)
    #halt movement in preparation for next function
    #segment 1
    segment1left.stop()
    segment1right.stop()
    #segment 2
    segment2left.stop()
    segment2right.stop()
    #segment 3
    segment3left.stop()
    segment3right.stop()
    sleep(2)
    
def climb():
    #function to be called for the climb demo
    #increase the speed + power output in an effort to make it
    #segment 1
    segment1left.backward()
    segment1right.forward()
    #segment 2
    segment2left.backward()
    segment2right.forward()
    #segment 3
    segment3left.backward()
    segment3right.forward()
    
def stop():
    #function that stops all motors at once
    #segment 1
    segment1left.stop()
    segment1right.stop()
    #segment 2
    segment2left.stop()
    segment2right.stop()
    #segment 3
    segment3left.stop()
    segment3right.stop()

#step code
def step_left():
    segment1left.backward(0.97) #backward due to wiring
    segment2right.forward(0.93)
    segment3left.backward(0.91) #backward due to
    
def step_right():
    segment1right.forward(0.93)
    segment2left.backward() #backward due to wiring
    segment3right.forward(0.94)
    
def step_motion():
    step_left()
    sleep(0.3)
    stop()
    sleep(0.3)
    step_right()
    sleep(0.3)
    stop()
    sleep(0.3)

x = 0
while x < 10:
     step_motion()
     x += 1