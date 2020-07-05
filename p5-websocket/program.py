import asyncio
import websockets
import sys

import pyaudio
import numpy as np
import wave
import speech_recognition as sr

CHUNK = 1024
RATE = 44100
CHANNELS = 2
FORMAT = pyaudio.paInt16

p=pyaudio.PyAudio()
stream=None

_Command = [
    ]

def SendToSvr(_msg):
    _port = sys.argv[2]
    _ip = sys.argv[1]
    async def hello(uri,msg):
        async with websockets.connect(uri) as websocket:
            await websocket.send(msg)
    asyncio.get_event_loop().run_until_complete(
            hello('ws://'+_ip+':'+_port,_msg))
def ConvertAudio(_stream):
    WAVE_OUTPUT_FILENAME = 'temp.wav'
    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(p.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

    return sr.AudioFile(WAVE_OUTPUT_FILENAME)

def StopRecord():
    stream.stop_stream()
    stream.close()
    p.terminate()
def StartRecord():
    stream = p.open(format=pyaudio.paInt16,channels=CHANNELS,rate=RATE,input=True,
              frames_per_buffer=CHUNK)

              
#### Start
while True:
    StartRecord()
    i = 0
    bars = 35
    maxValue = 2**16
    frames = []
    while i<int((44100/1024)/2):
        data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
        dataL = data[0::2]
        dataR = data[1::2]
        peakL = np.abs(np.max(dataL)-np.min(dataL))/maxValue
        peakR = np.abs(np.max(dataR)-np.min(dataR))/maxValue
        lString = "#"*int(peakL*bars)+"-"*int(bars-peakL*bars)
        rString = "#"*int(peakR*bars)+"-"*int(bars-peakR*bars)
        frames.append(data)
        peak=np.average(np.abs(data))*2
        b="#"*int(50*peak/2**16)

        print("L=[%s]\tR=[%s]"%(lString, rString))
        i = 0 if len(b)!=0 else i +1

    r = sr.Recognizer()
    with ConvertAudio(frames) as source:
        audio = r.record(source)
    try:
        _text = r.recognize_google(audio)
        print(_text)
    except:
        print("Noisy audio")
    StopRecord()
exit()
#### END


frames = []
while i<int(44100/1024):
    print(i)
    data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
    peak=np.average(np.abs(data))*2
    bars="#"*int(50*peak/2**16)
    frames.append(data)
    i = 0 if len(bars)!=0 else i
    print(i)
    #print("this is bar {}".format(str(len(bars))))
    #print(i)
    #print("%04d %05d %s"%(i,peak,bars))
    i = i+1
r = sr.Recognizer()
_audio = r.record(stream)
_text = r.recognize_google(_audio)
stream.stop_stream()
stream.close()
p.terminate()

exit()
_out = b''.join(frames)
print(_out)
_audio = r.record(_out)
_text = r.recognize_google(_audio)
'''



exit()
_audio = r.record(_out)
_text = r.recognize_google(_audio)
'''
waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(p.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()
'''

'''
while True:
    for i in range(int(10*44100/1024)): #go for a few seconds
        data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
        peak=np.average(np.abs(data))*2
        bars="#"*int(50*peak/2**16)
        print("%04d %05d %s"%(i,peak,bars))
'''


