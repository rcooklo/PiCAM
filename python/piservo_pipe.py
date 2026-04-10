#!/usr/bin/env python3
 
import time
import os, sys
import piservo
 
p_servo = piservo.PiServo()
panval = 90
tiltval = 90
oldpanval = 90
oldtiltval = 90
min_pan = 0
max_pan = 180
min_tilt = 0
max_tilt = 180

 
while True:
  pipein = open("/home/pi/python/FIFO_piservo", 'r')
  line = pipein.readline()
  line_array = line.split(' ')
  if line_array[0] == "servo":
    panval = int(line_array[1])
    tiltval = int(line_array[2])
    if panval < min_pan:
        panval = min_pan
    if panval > max_pan:
        panval = max_pan
    if tiltval < min_tilt:
        tiltval = min_tilt
    if tiltval > max_tilt:
        tiltval = max_tilt

    if panval > oldpanval:
        for x in range(oldpanval, panval):
            p_servo.do_pan(x)
            time.sleep(0.01)
    if oldpanval > panval:
        for x in range(oldpanval, panval, -1):
            p_servo.do_pan(x)
            time.sleep(0.01)
    #p_servo.do_tilt(tiltval)
    if tiltval > oldtiltval:
        for x in range(oldtiltval, tiltval):
            p_servo.do_tilt(x)
            time.sleep(0.01)
    if oldtiltval > tiltval:
        for x in range(oldtiltval, tiltval, -1):
            p_servo.do_tilt(x)
            time.sleep(0.01)

#    print(panval, tiltval)
    oldpanval = panval
    oldtiltval = tiltval

  if line_array[0] == "change":
    panval = oldpanval + int(line_array[1])
    tiltval = oldtiltval + int(line_array[2])
    if panval < min_pan:
        panval = min_pan
    if panval > max_pan:
        panval = max_pan
    if tiltval < min_tilt:
        tiltval = min_tilt
    if tiltval > max_tilt:
        tiltval = max_tilt

    if panval > oldpanval:
        for x in range(oldpanval, panval):
            p_servo.do_pan(x)
            time.sleep(0.01)
    if oldpanval > panval:
        for x in range(oldpanval, panval, -1):
            p_servo.do_pan(x)
            time.sleep(0.01)
    #p_servo.do_tilt(tiltval)
    if tiltval > oldtiltval:
        for x in range(oldtiltval, tiltval):
            p_servo.do_tilt(x)
            time.sleep(0.01)
    if oldtiltval > tiltval:
        for x in range(oldtiltval, tiltval, -1):
            p_servo.do_tilt(x)
            time.sleep(0.01)

#    print(panval, tiltval)
    oldpanval = panval
    oldtiltval = tiltval
  pipein.close()
