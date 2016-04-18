#! /usr/bin/env python
# Author:	Gopal Krishan Aggarwal 
# Contact: 	gopalkriagg@gmail.com
# Desc: 	This script check wind direction every 10 seconds for 3 minutes and then stores the average wind direction in windDirection.txt file.
from time import sleep
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC
ADC.setup()
import os
cwd = os.path.dirname(os.path.realpath(__file__))
windVanePin = "P9_33"
directionSum = 0               #Maintains the sum of wind direction after every 10 seconds
directionCount = 0
time = 3 * 60

def IncDirectionSum():
    global directionCount, directionSum
    value = ADC.read(windVanePin)
    value = ADC.read(windVanePin) #Read twice due to bug as mentioned in ADC's documentation
    directionCount += 1
    if (value > 0.865331565 and value <  0.885331565) :
        directionSum += 0
    elif (value > 0.5729636202 and value <  0.5929636202) :
        directionSum += 22.5
    elif (value > 0.6256589147 and value <  0.6456589147) :
        directionSum += 45
    elif (value > 0.1493632624 and value <  0.1654385965) :
        directionSum += 67.5
    elif (value > 0.1654385965 and value <  0.1854385965) :
        directionSum += 90
    elif (value > 0.1176911656 and value <  0.1376911656) :
        directionSum += 112.5
    elif (value > 0.3088405797 and value <  0.3288405797) :
        directionSum += 135
    elif (value > 0.2207692308 and value <  0.2407692308) :
        directionSum += 157.5
    elif (value > 0.4434883721 and value <  0.4634883721) :
        directionSum += 180
    elif (value > 0.3905102041 and value <  0.4105102041) :
        directionSum += 202.5
    elif (value > 0.7629468599 and value <  0.7829468599) :
        directionSum += 225
    elif (value > 0.7402656748 and value <  0.7602656748) :
        directionSum += 247.5
    elif (value > 0.9523095429 and value <  0.9723095429) :
        directionSum += 270
    elif (value > 0.8896155489 and value <  0.9096155489) :
        directionSum += 292.5
    elif (value > 0.9224712644 and value <  0.9424712644) :
        directionSum += 315
    elif (value > 0.8131753198 and value <  0.8331753198) :
        directionSum += 337.5
    else :
        directionCount -= 1


def resetWindDirectionReading():
    global directionCount, directionSum
    directionSum = 0
    directionCount = 0
    
def getWindDirectionReading():
    return directionSum / directionCount
    
def chorus():
	f = open(cwd+'/windDirectionReading.txt', 'w', 0)
	f.write(str(getWindDirectionReading()))
	resetWindDirectionReading()
	f.close()

count = 0
while True:
	sleep(10)		#Sleep for 10 seconds
	IncDirectionSum()
	count += 1
	if(count == time/10) :
	    chorus()		#perform this chorus
	    count = 0
	    
	