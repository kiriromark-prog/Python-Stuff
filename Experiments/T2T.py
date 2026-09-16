import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Set speech rate
engine.say("Hello, I am your text to speech engine.")
engine.runAndWait()