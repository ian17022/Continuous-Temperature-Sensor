 #Python
#Libraries
import RPi.GPIO as GPIO
import time
from RpiMotorLib import RpiMotorLib
import os
import glob
from datetime import datetime


filename = "Results.txt" # Change this to the filename to be created 
#### for height sensor ####
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

#set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 25

#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2

    return distance
### End of height sensor code ### 

### Temperature sensor code ### 
def read_temp(decimals = 1, sleeptime = 3):
     # """Reads the temperature from a 1-wire device"""
    device = glob.glob("/sys/bus/w1/devices/" + "28*")[0] + "/w1_slave"
    with open(device, "r") as f:
        lines = f.readlines()
    while lines[0].strip()[-3:] != "YES":
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find("t=")
    if equals_pos != -1:
        f = open(filename,"a+")
        temp_string = lines[1][equals_pos+2:]
        temp = round(float(temp_string) / 1000.0, 3)
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S") # Formating the time
        dist = distance()
        print("Temp = {} [deg]\ttime = {}\theight = {}[cm]\n".format(temp,dt_string,dist)) #Printing results to the terminal
        f.write("{}\t{}\t{}\n".format(temp,dt_string,dist)) # Writing results to text file
        f.close()

if __name__ == '__main__':
    try:
        f = open("temperature.txt","a+")
        for i in range(10):
            read_temp()
            time.sleep(1)
            print("measurement " + str(i) + " is completed \n") 
        f.close()
        print("measurement completed \n")
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("\n Measurement stopped by User")
        f = open("temperature.txt","a+")
        f.close()
        GPIO.cleanup()
        exit( 1 )
GPIO.cleanup()
