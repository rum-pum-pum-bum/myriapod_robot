from picozero import Motor
from picozero import Robot
from picozero import RGBLED
from time import sleep

#turn each sequence into a function?
#trigger different functions w/ button push?
#need small breadboards for wiring ^
#video of the LED model + actual model
#add schematics for LED temp setup to report
#RGB setup + DC motor setup

#initializing motors for individual motor control
segment1left = Motor(10,11) #pin numbers go here
segment1right = Motor(12,13)
#segment2left = Motor(14,15)
#segment2right = Motor(16,17)
#segment3left = Motor(18,19)
#segment3right = Motor(20,21)

#initializing robot function to control 2 motors simultaneously
segment1 = Robot(left=(10,11), right=(12,13)) #pin numbers for both motors go here
#segment2 = Robot(left=(14,15), right=(16,17))
#segment3 = Robot(left=(18,19), right=(20,21))

#initializing LEDs for troubleshooting segment 1
rgb = RGBLED(red = 1, green = 2, blue = 3)

#turn on sequence
#push button to turn on [add code]
print('hello! I am here to help')
rgb.on() #white

#movement forward
#segment 1
segment1.forward(0.5) #0.5 = half speed
rgb.color(0, 255, 0) #green
#segment 2
#segment2.forward(0.5)
#segment 3
#segment3.forward(0.5)
sleep(10) #run the forward sequence for 10 seconds
print('here we go!')

#right turn sequence
print('turning right!')
segment1.stop() #stop the united motion
segment1left.forward(0.5) #left keeps full speed
segment1right.forward(0.35) #right decreases speed slightly for wide turn
rgb.color(255, 0, 0) #red
sleep(10) #turn for 10 seconds
#add other segments to turn at a delayed sequence

#end turn sequence
#bring speeds to same slightly slower speed
segment1left.forward(0.45)
segment1right.forward(0.45)
rgb.color(255, 255, 0) #yellow
sleep(10) #keep this speed for 10 seconds to allow for the other segments to catch up
#segment2left.forward(0.45)
#segment2right.forward(0.45)
#sleep(8) #delay for less seconds as the segments will unite in sequence
#segment3left.forward(0.45)
#segment3right.forward(0.45)
#sleep(6) #delay for less seconds as the segments will unite in sequence
segment1left.stop() #halting all movement
segment1right.stop()
rgb.off()
#segment2left.stop()
#segment2right.stop()
#segment3left.stop()
#segment3right.stop()

#return to straight motion
segment1.forward(0.5)
rgb.color(0, 255, 0)
print('back in business, baby')
#segment2.forward(0.5)
#segment3.forward(0.5)
sleep(10) #keep forward motion for 10 seconds

#left turn sequence
print('turning left!')
segment1.stop() #stop united motion
segment1left.forward(0.35) #left decreases speed slightly for wide turn
segment1right.forward(0.5) #right keeps full speed
rgb.color(255, 255, 0)
sleep(10) #run the turn for 10 seconds
#add other segments to turn at a delayed sequence

#end turn sequence
#bring speeds to same slightly slower speed
segment1left.forward(0.45)
segment1right.forward(0.45)
rgb.color(255, 255, 0) #yellow
sleep(10) #keep this speed for 10 seconds to allow for the other segments to catch up
#segment2left.forward(0.45)
#segment2right.forward(0.45)
#sleep(8) #delay for less seconds as the segments will unite in sequence
#segment3left.forward(0.45)
#segment3right.forward(0.45)
#sleep(6) #delay for less seconds as the segments will unite in sequence
segment1left.stop() #halting all movement
segment1right.stop()
rgb.off()
#segment2left.stop()
#segment2right.stop()
#segment3left.stop()
#segment3right.stop()

#return to straight motion
segment1.forward(0.5)
rgb.color(0, 255, 0)
print('back in business, baby')
#segment2.forward(0.5)
#segment3.forward(0.5)
sleep(10) #keep forward motion for 10 seconds

#climb sequence
print('up we go')
segment1.forward(0.75) #needs more speed for more power and so it is less likely to get stuck
#segment2.forward(0.75)
#segment3.forward(0.75)
sleep(10) #hold motion style
segment1.stop()
#segment2.stop()
#segment3.stop()

#end sequence
segment1.stop()
rgb.off()
print('I do not want to die')
#segment2.stop() #stop segment 2
print('but okay')
#segment3.stop() #stop segment 3
print('goodbye T^T')