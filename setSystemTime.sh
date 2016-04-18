#!/bin/bash
echo ds3231 0x68 > /sys/bus/i2c/devices/i2c-1/new_device
/sbin/hwclock -f /dev/rtc1 -s
date