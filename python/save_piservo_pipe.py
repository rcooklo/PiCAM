#!/usr/bin/env python3
 
import time
import os, sys
import piservo
 
p_servo = piservo.PiServo()
 
while True:
  pipein = open("/home/pi/python/FIFO_piservo", 'r')
  line = pipein.readline()
  line_array = line.split(' ')
  if line_array[0] == "servo":
    p_servo.do_pan(int(line_array[1]))
    p_servo.do_tilt(int(line_array[2]))
  pipein.close()

