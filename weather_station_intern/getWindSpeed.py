#! /usr/bin/env python
# Author:	Gopal Krishan Aggarwal and Piyush Mangtani
# Contact: 	gopalkriagg@gmail.com
# Desc: 	For waitingTime seconds it checks how many times anemometer rotates and thus calculates the average speed in those waitingTime seconds. Read more at the sparfun's weather meter datasheet.
from time import sleep
import RPi.GPIO as GPIO
anemometerPin = 15				#Declaring the GPIO pin for wind speed
waitingTime = 2					#in seconds
GPIO.setmode(GPIO.BOARD)
GPIO.setup(anemometerPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#print("The script is running ")

anemometerSwitchCount = 0			#Maintains the count of number of switch closes

def AnemometerSwitchCount(y):			#anemometerSwitchCount increments the count of anemometer switch closes
        global anemometerSwitchCount 	
	anemometerSwitchCount += 1        

def getWindSpeed():
	try:
		GPIO.add_event_detect(anemometerPin, GPIO.FALLING, callback = AnemometerSwitchCount , bouncetime = 100)
       	except:
                GPIO.add_event_detect(anemometerPin, GPIO.FALLING, callback = AnemometerSwitchCount , bouncetime = 100)
	sleep(waitingTime)				#Now for these 5 seconds each falling interrupt will cause 

        windSpeed = 2.4*anemometerSwitchCount/(2.0*waitingTime)			#Since speed is 2.4km/hr per switch close and
       
	sleep(1)
	GPIO.remove_event_detect(anemometerPin)	#Since event/interrupt detection is not needed now
	return windSpeed

f = open('/home/pi/weatherStation/windSpeed.txt', 'w', 0)
windSpeed = getWindSpeed()
f.write(str(windSpeed))
print windSpeed
f.close()
sleep(1)
GPIO.cleanup()
