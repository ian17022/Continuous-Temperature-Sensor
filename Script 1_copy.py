import RPi.GPIO as GPIO
import time
from RpiMotorLib import RpiMotorLib
import os
import glob
from datetime import datetime
import math

#define GPIO pins
direction= 22 # Direction (DIR) GPIO Pin
step = 23 # Step GPIO Pin
EN_pin = 24 # enable pin (LOW to enable)

# Declare a instance of class pass GPIO pins numbers and the motor type
mymotortest = RpiMotorLib.A4988Nema(direction, step, (21,21,21), "DRV8825")
GPIO.setup(EN_pin,GPIO.OUT) # set enable pin as output

GPIO.output(EN_pin,GPIO.LOW) # pull enable to low to enable motor
mymotortest.motor_go(True, # True=Clockwise, False=Counter-Clockwise
                     "Full" , # Step type (Full,Half,1/4,1/8,1/16,1/32)
                     500, # number of steps to move 10cm distance
                     .001, # step delay [sec]
                     False, # True = print verbose output
                     .05) # initial delay [sec]

GPIO.cleanup()
