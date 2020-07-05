import sys

import pyaudio
import numpy as np
import wave
import speech_recognition as sr

class Program:
    CHUNK = 1024
    RATE = 44100
    CHANNELS = 2
    FORMAT = pyaudio.paInt16

    p = None
    stream = None

    def ConvertAudio(self,_frame):
        WAVE_OUTPUT_FILENAME = 'temp.wav'
        waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        waveFile.setnchannels(self.CHANNELS)
        waveFile.setsampwidth(self.p.get_sample_size(self.FORMAT))
        waveFile.setframerate(self.RATE)
        waveFile.writeframes(b''.join(_frame))
        waveFile.close()

        return sr.AudioFile(WAVE_OUTPUT_FILENAME)

    def StopRecord(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
    def StartRecord(self):
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=pyaudio.paInt16,channels=self.CHANNELS,rate=self.RATE,input=True,
                frames_per_buffer=self.CHUNK)

    def __init__(self):
        #### Start
        while True:
            self.StartRecord()
            
            i = 0
            bars = 35
            maxValue = 2**16
            frames = []
            _tf = False
            while i<int((44100/1024)):
                data = np.fromstring(self.stream.read(self.CHUNK),dtype=np.int16)
                dataL = data[0::2]
                dataR = data[1::2]
                peakL = np.abs(np.max(dataL)-np.min(dataL))/maxValue
                peakR = np.abs(np.max(dataR)-np.min(dataR))/maxValue
                lString = "#"*int(peakL*bars)+"-"*int(bars-peakL*bars)
                rString = "#"*int(peakR*bars)+"-"*int(bars-peakR*bars)
                frames.append(data)
                peak=np.average(np.abs(data))*2
                b="#"*int(50*peak/2**16)

                print("L=[%s]\t\tR=[%s]"%(lString, rString))
                i = 0 if len(b)!=0 else i +1
                if len(b)!=0:
                    _tf = True

            if _tf:
                r = sr.Recognizer()
                audio = None
                with self.ConvertAudio(frames) as source:
                    audio = r.record(source)
                try:
                    #_text = r.recognize_google(audio,language='en-gb')
                    #_text = r.recognize_google(audio)
                    _text = r.recognize_sphinx(audio)
                    print(_text)
                    exit()
                except:
                    #pass
                    print("Noisy audio")
            _tf = False    
            self.StopRecord()
        exit()
        #### END
#Start Point    
Program()