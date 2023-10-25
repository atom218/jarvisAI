import speech_recognition as sr
import os

def say(text):
    os.system(f"say {text}")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        query = r.recognize_google(audio, language="en-in")
        print(f"user said: {query}")
        return query

if __name__ == "__main__":
    print("Jarvis")
    say("Hello, I am Jarvis A.I")
    print("Listening...")
    text = takeCommand()
    say(text)
