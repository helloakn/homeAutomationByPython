# Import the required module for text 
# to speech conversion
from gtts import gTTS
 
# This module is imported so that we can 
# play the converted audio
import os
 
# The text that you want to convert to audio
mytext = 'hay hein ko, hay hein ko. Fuck you, Love you, Fuck you, very Fuck you baby, suck my cock!'
 
# Language in which you want to convert
language = 'en'
 
# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)
 
# Saving the converted audio in a mp3 file named
# welcome 
myobj.save("welcome.mp3")
 
# Playing the converted file
import pygame, time
pygame.init()
pygame.mixer.music.load('welcome.mp3')
pygame.mixer.music.play()
time.sleep(5)
pygame.mixer.music.fadeout(5)

#os.system("mpg321 welcome.mp3")
