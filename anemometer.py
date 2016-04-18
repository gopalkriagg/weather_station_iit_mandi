#! /usr/bin/env python
# Author:	Gopal Krishan Aggarwal 
# Contact: 	gopalkriagg@gmail.com
# Desc: 	This script must run at boot time. It continously counts number of switch closes and after every 3 mins stores the wind speed in windReading.txt file and resets the swtichCloses counter. i.e. it stores the average wind speed in last 3 mins in windRading.txt file.
from time import sleep
import Adafruit_BBIO.GPIO as GPIO

import os
cwd = os.path.dirname(os.path.realpath(__file__))
anemometerPin = "P9_15"
switchCloses = 0               #Maintains the count of how many times bucket inside rain gauge tipped
time = 3 * 60

GPIO.setup(anemometerPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#IncSwitchClosesCount() increments the count of switchCloses
def IncSwitchClosesCount(y):
        global switchCloses
        switchCloses += 1
	print "Switch Closed"

try:
	GPIO.add_event_detect(anemometerPin, GPIO.FALLING, callback = IncSwitchClosesCount, bouncetime = 100)
except:
    GPIO.add_event_detect(anemometerPin, GPIO.FALLING, callback = IncSwitchClosesCount, bouncetime = 100)

def resetWindReading():
	global switchCloses
	switchCloses = 0

def getWindReading():
	windSpeed =  ( switchCloses * 2.4 ) / (2 * time) #Refer https://www.sparkfun.com/datasheets/Sensors/Weather/Weather%20Sensor%20Assembly..pdf
	return windSpeed	#Wind in millimeters in last 3 minutes

def chorus():
	f = open(cwd+'/windSpeedReading.txt', 'w', 0)
	f.write(str(getWindReading()))
	resetWindReading()
	f.close()

while True:
	sleep(time)		#After every 3 minutes 
	chorus()		#perform this chorus