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
try:
            text = r.recognize_google(audio)
            print("You said:", text)
            return text
        except sr.UnknownValueError:
            print("Sorry, I didn't understand.")
            return ""
        except sr.RequestError:
            print("Sorry, I couldn't connect to the speech recognition service.")
            return ""

open_pattern = re.compile(r"open")
search_pattern = re.compile(r"search")
tell_pattern = re.compile(r"tell me about")
time_pattern = re.compile(r"time")

def open_application(app_name):
    try:
        subprocess.Popen(["start", " ", app_name], shell=True)
    except Exception as e:
        print(f"Error opening application: {e}")

