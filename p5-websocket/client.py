
import asyncio
import websockets
import sys

import speech_recognition as sr

r = sr.Recognizer()

import pyttsx3
engine  = pyttsx3.init()

engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')
engine.say("hello world, I'm robotic.")
engine.runAndWait()


_port = sys.argv[2]
_ip = sys.argv[1]

async def hello(uri,msg):
    async with websockets.connect(uri) as websocket:
        await websocket.send(msg)
asyncio.get_event_loop().run_until_complete(
        hello('ws://'+_ip+':'+_port,"hello"))
'''
while True:
    try:
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
        inputText = r.recognize_google(audio)
        print(inputText)
        asyncio.get_event_loop().run_until_complete(
        hello('ws://'+_ip+':'+_port,inputText))
    except:
        print("try again!")
    
    '''

