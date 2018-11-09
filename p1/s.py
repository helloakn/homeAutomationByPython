import sys
import pyttsx3
engine = pyttsx3.init()
engine.say(sys.argv[1])
engine.runAndWait()
