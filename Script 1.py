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

s = input("How many cm would you like to go?\n (negative number for down and positive for up\n")
try:
    s = float(s)
except:
    print("input must be a non-zero number")
    GPIO.cleanup()
    exit ( 1 )

if s > 0:
    p = True
elif s < 0:
    p = False
    s = -s
s = s * 50
s = math.floor(s)
GPIO.output(EN_pin,GPIO.LOW) # pull enable to low to enable motor
mymotortest.motor_go(True, # True=Clockwise, False=Counter-Clockwise
                     "Full" , # Step type (Full,Half,1/4,1/8,1/16,1/32)
                     s, # number of steps
                     .001, # step delay [sec]
                     False, # True = print verbose output
                     .05) # initial delay [sec]

GPIO.cleanup()
