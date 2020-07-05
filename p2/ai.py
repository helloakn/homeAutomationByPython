'''
for multi processing
'''
import _thread
import time
'''
for multi processing
'''
import pyttsx3
engine  = pyttsx3.init()

engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')
engine.say("Greeting the World! let's start the game.")
engine.runAndWait()


# Define a function for the thread
def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

# Create two threads as follows
try:
   _thread.start_new_thread( print_time, ("Thread-1", 1, ) )
   _thread.start_new_thread( print_time, ("Thread-2", 4, ) )
except:
   print ("Error: unable to start thread")

while 1:
   pass