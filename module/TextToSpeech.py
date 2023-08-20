import pyttsx3


def play(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
