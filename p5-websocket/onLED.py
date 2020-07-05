
import sys
import RPi.GPIO as GPIO
import time


_action = sys.argv[1]


def lightOff(pinNumber):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.output(pinNumber,GPIO.LOW)
    

def lightOn(pinNumber):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(pinNumber,GPIO.OUT)
    GPIO.output(pinNumber,GPIO.HIGH)
if _action == 'on':
    lightOn(17)
    lightOn(18)
    lightOn(23)
    lightOn(24)
else:
    lightOff(17)
    lightOff(18)
    lightOff(23)
    lightOff(24)


    