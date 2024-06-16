import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import subprocess 
import os
import re

# Initialize the speech recognition engine
r = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Define a function to speak the given text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Define a function to listen to user input
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
