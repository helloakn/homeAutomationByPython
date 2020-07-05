#text to speech
import pyttsx3
engine  = pyttsx3.init()

engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')
engine.say("Greeting the World! let's start the game.")
engine.runAndWait()

#speech recognize
'''
com.apple.speech.synthesis.voice.daniel
com.apple.speech.synthesis.voice.moira
com.apple.speech.synthesis.voice.samantha
'''
'''
voices = engine.getProperty('voices')
for voice in voices:
    print(voice, voice.id)
    engine.setProperty('voice', voice.id)

    engine.say("Hello World!")
    engine.runAndWait()
    engine.stop()
'''
import speech_recognition as sr


r = sr.Recognizer()
while True:
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    inputText = r.recognize_google(audio)
    print(inputText)
    engine.say(inputText)
    engine.runAndWait()

'''
# recognize speech using Sphinx
try:
    print("Sphinx thinks you said " + r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))
'''