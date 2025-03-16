
import pyttsx3
import speech_recognition
import requests
from bs4 import BeautifulSoup
import datetime
import pyautogui
import os
import my_keyboard
import random
import webbrowser
import NewsRead
import socketio
sio = socketio.Client()

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 300) 

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 0.5
        r.energy_threshold = 100
        audio = r.listen(source, 0, 4)

    try:
        print("Understanding..")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
        return query.lower()  # Ensure lowercase for consistency
    except Exception as e:
        print("Say that again")
        return "None"
def alarm(query):
     timehere = open("Alarmtext.txt","a")
     timehere.write(query)
     timehere.close()
     os.startfile("alarm.py")
if __name__ == "__main__":  
    while True:  
        query = takeCommand()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand()

                if "go to sleep" in query:  # ✅ Fixed condition
                    speak("Ok sir, You can call me anytime")
                    print("Sleeping mode activated.")  
                    break  # Exits only after speaking
                
                elif "hello" in query:
                    speak("Hello sir, how are you?")
                elif "i am fine" in query:
                    speak("That's great, sir")
                elif "how are you" in query:
                    speak("Perfect, sir")
                elif "thank you" in query:
                    speak("You're welcome, sir")
                elif "tired" in query:
                   speak("Playing your favourite songs, sir")
                   a = (1,2,3)
                   b = random.choice(a)
                   if b==1:
                    webbrowser.open("https://www.youtube.com/watch?v=TVbI55pDdaI")
                elif "news" in query:
                  from NewsRead import latestnews
                  latestnews()
                
                elif "pause" in query:
                 pyautogui.press("k")
                 speak("video paused")
                elif "play" in query:
                 pyautogui.press("k")
                 speak("video played")
                elif "mute" in query:
                 pyautogui.press("m")
                 speak("video muted")

                elif "volume up" in query:
                 from my_keyboard import volumeup
                 speak("Turning volume up,sir")
                 volumeup()
                elif "volume down" in query:
                 from my_keyboard import volumedown
                 speak("Turning volume down, sir")
                 volumedown()

                elif "open" in query:
                  from Dictapp import openappweb
                  openappweb(query)
                elif "close" in query:
                   from Dictapp import closeappweb
                   closeappweb(query)

                elif "google" in query:
                 from SearchNow import searchGoogle
                 searchGoogle(query)
                elif "youtube" in query:
                 from SearchNow import searchYoutube
                 searchYoutube(query)
                elif "wikipedia" in query:
                  from SearchNow import searchWikipedia
                  searchWikipedia(query)

                elif "temperature" in query:
                 search = "temperature in delhi"
                 url = f"https://www.google.com/search?q={search}"
                 r  = requests.get(url)
                 data = BeautifulSoup(r.text,"html.parser")
                 temp = data.find("div", class_ = "BNeawe").text
                 speak(f"current{search} is {temp}")

                elif "weather" in query:
                  search = "temperature in delhi"
                  url = f"https://www.google.com/search?q={search}"
                  r  = requests.get(url)
                  data = BeautifulSoup(r.text,"html.parser")
                  temp = data.find("div", class_ = "BNeawe").text
                  speak(f"current{search} is {temp}") 
                elif "set an alarm" in query:
                  print("input time example:- 10 and 10 and 10")
                  speak("Set the time")
                  a = input("Please tell the time :- ")
                  alarm(a)
                  speak("Done,sir")               
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"Sir, the time is {strTime}")
                elif "finally sleep" in query:
                 speak("Going to sleep,sir")
                 exit()
                elif "remember that" in query:
                 rememberMessage = query.replace("remember that","")
                 rememberMessage = query.replace("jarvis","")
                 speak("You told me to remember that"+rememberMessage)
                 remember = open("Remember.txt","a")
                 remember.write(rememberMessage)
                 remember.close()
                elif "what do you remember" in query:
                 remember = open("Remember.txt","r")
                 speak("You told me to remember that" + remember.read())
                 # 🔹 HAND GESTURE DETECTION INTEGRATION
                elif "recognize my hand" in query:
                    speak("Starting hand gesture recognition, sir.")
                    sio.emit('start_gesture')  # 🔹 Tell WebSocket to start detection
                
                elif "stop recognition" in query:
                    speak("Stopping hand gesture recognition, sir.")
                    sio.emit('stop_gesture')  # 🔹 Tell WebSocket to stop detection