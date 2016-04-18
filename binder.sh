#!/usr/bin/env bash
pwd="/root/weather_station_iit"

DHTTempHumidity=`python $pwd/Adafruit_Python_DHT/examples/AdafruitDHT_modified.py 22 P9_12`; #Runs the script mentioned in backticks and stores the result in the variable. 11 specifies that DHT22 is being used and P9_12 specifies it is connected to pin P9_12 of BBB. Visit the Adafruit website for more details.
echo $DHTTempHumidity

BMPPressureTemp=`python $pwd/Adafruit_Python_BMP/examples/simpletest_modified.py`; #Similar to above for BMP pressure sensor.

echo $BMPPressureTemp

RainGaugeReading=`cat $pwd/rainReading.txt` #The script rainfall.py which was run at boot-time stores the result in rainReading.txt every 3 mins. Here we are fetching that reading and storing it in the variable.

WindSpeedReading=`cat $pwd/windSpeedReading.txt` 

WindDirection=`cat $pwd/windDirectionReading.txt`

echo "Rain Gauge Reading is: $RainGaugeReading"
echo "Wind speed is: $WindSpeedReading"
echo "Wind direction is: $WindDirection"
echo `date`
printf "`hostname`,$DHTTempHumidity,$BMPPressureTemp,$RainGaugeReading,$WindSpeedReading,$WindDirection,`date`,\n" >> /root/weather_station_iit/weather.data


# BETTER OPTION (prevents the conflict of multiple scripts writing on same file):
# At this point of time we have latest weather data appended to weatherLocalCopy.data and
# we also have another identical file weatherPhant.data which we will use to upload data
# to phant. The algo goes as follows:
# 1) Check if script phant-loggerGSM.py is running
#	Case 'no':It is not running. This case should occur only when there is only one
#		row of weather data (i.e. the latest one) is left for uploading which is GOOD! In some
#		rare scenario it might happen that we enter this 'yes' case yet there is no
#		row of data in file to be uploaded -- or can't it?
# 		i) In this case run the script phant-loggerGSM.py
#	Case 'yes' : i.e. script phant-loggerGSM.py is already running! This would be because
# 		the script is trying to upload previous data only.
# 		i)Don't do anything since previously running phant-logger.py will handle the
# 		 latest data too.

process=`ps aux | grep 'phant-loggerGSM.py' | wc -l`	#Check if phant-loggerGSM.py is already running
echo $process #If result is 2 then phant-loggerGSM.py is running
if [ $process -eq 1 ]; then #If phant-loggerGSM.py is not running then run it to upload the latest reading
	echo "Going to run phant-loggerGSM.py"
	#python "$pwd/phant-loggerGSM.py"
else
	echo "Seems like phant-loggerGSM.py is already running" #If phant-loggerGSM.py is already running it means it is trying to upload previous readings.
fi