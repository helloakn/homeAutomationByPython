import asyncio
import websockets

import sys
import RPi.GPIO as GPIO
import time

import pyttsx # text to speech
'''
import pyttsx3
engine  = pyttsx3.init()

engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')
engine.say("hello world, I'm robotic.")
engine.runAndWait()
'''
_port = sys.argv[2]
_ip = sys.argv[1]

'''
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(14,GPIO.OUT)
print "LED on"
GPIO.output(14,GPIO.HIGH)
time.sleep(1)
print "LED off"
GPIO.output(14,GPIO.LOW)
on = 1
off = 0
white = 18
yellow = 17
red = 23
twocolor = 24
'''

def lightOff(pinNumber):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.output(pinNumber,GPIO.LOW)
    

def lightOn(pinNumber):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(pinNumber,GPIO.OUT)
    GPIO.output(pinNumber,GPIO.HIGH)

def speak(_text):
    engine = pyttsx.init()
    engine.say(_text)
    engine.runAndWait()

async def echo(websocket, path):
    name = await websocket.recv()
    print("-> {}".format(name))
    name = name.lower()
    if 'yellow color of' in name:
        lightOff(17)
        text = " ok sir, finished "
        speak(text)
    elif 'yellow color on' in name:
        lightOn(17)
        text = " ok sir, finished "
        speak(text)

    elif 'white color of' in name:
        lightOff(18)
        text = " ok sir, finished "
        speak(text)

    elif 'white color on' in name:
        lightOn(18)
        text = " ok sir, finished "
        speak(text)

    elif 'red color of' in name:
        lightOff(23)
        text = " ok sir, finished "
        speak(text)

    elif 'red color on' in name:
        lightOn(23)
        text = " ok sir, finished "
        speak(text)
    
    elif 'green color of' in name:
        lightOff(24)
        text = " ok sir, finished "
        speak(text)

    elif 'green color on' in name:
        lightOn(24)
        text = " ok sir, finished "
        speak(text)

    #speaking
    elif 'who are you' in name:
        text = " I'm Sakura. "
        speak(text)
    
    elif 'who create you' in name:
        text = "Super Genius F A, akn "
        speak(text)
    
    elif 'who created you' in name:
        text = "Super Genius F A, akn "
        speak(text)
        

asyncio.get_event_loop().run_until_complete(
    websockets.serve(echo, _ip, int(_port)))
asyncio.get_event_loop().run_forever()


    