import pyttsx3 
import speech_recognition as sr 
import datetime
import pytz
import wikipedia 
import webbrowser
import os
import smtplib
import pyautogui
import subprocess
import re
import requests
import time
from ecapture import ecapture as ec
import winapps
import winshell
import ctypes
import win32com.client as wincl



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query




if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if "goodbye" in query or "ok bye" in query or "stop" in query:
                print('Your virtual assistant Jarvis is shutting down,Good bye')
                speak('your virtual assistant Jarvis is shutting down,Good bye')
                break

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        #elif 'open drive' or 'open disc' in query:
          #      speak("Which drive you have to open")
             #   statement=takeCommand()
             #   if "C" in statement or "c" in statement: 
             #       os.startfile("C:") 
    

              #  elif "D" in statement or "d" in statement: 
              #      os.startfile("D:") 
  

               # elif "E" in statement or "e" in statement: 
               #     os.startfile("E:") 
  
               # else: 
               #     print("Wrong Input")

        elif 'open youtube' in query:
            webbrowser.open_new_tab("https://www.youtube.com")
            print("Youtube is open now")
            speak("youtube is open now")

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("Google chrome is open now")

        elif 'open gmail' in query:
                webbrowser.open_new_tab("https://bit.ly/3iOcR5z")
                print("Google Mail opening now")
                speak("Google Mail opening now")  

        elif 'news' in query:
                news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
                speak('Here are some headlines for you')

        elif "weather" in query:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_temperature_celsius=(current_temperature-273.15)
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n Temperature in celsius is"+
                      str(current_temperature_celsius)+
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n Temperature in celsius unit is="+
                      str(current_temperature_celsius)+
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")
        
        elif 'play music' in query:
            music_dir = ''
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
            print (current_time)
            speak(str(current_time.hour)+'hour'+str(current_time.minute)+'minutes')

        elif 'open chrome' in query:
              chromePath = "C:\Program Files (x86)\Google\Chrome\Application\chrome"
              os.startfile(chromePath)
        
        elif 'change tab' in query:
              pyautogui.keyDown("alt")
              pyautogui.press("tab")
              pyautogui.keyUp("alt")

        elif 'open calculator' in query:
            subprocess.Popen('C:\\Windows\\System32\\calc.exe')
            
        elif 'open notepad' in query:
          subprocess.Popen('C:\\Windows\\System32\\notepad.exe')
        
        elif "log off" in query or "sign out" in query:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

        elif "camera" in query or "take a photo" in query or "capture"in query:
            #date_string = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M")
            ec.capture(0,"robo camera","img.jpg")

        elif 'show all installed apps' in query:
            for app in winapps.list_installed():
                print(app)     
                print("\n\n")
                #speak(app)
        
        elif 'search software' in query:
            speak('Which software do you want to search')
            soft=takeCommand()
            for app in winapps.search_installed(soft):
                print(app)
        
        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('note.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
         
        elif "show note" in query:
            speak("Showing Notes")
            file = open("note.txt", "r") 
            print(file.read())
            speak(file.read(6))

        elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()
 
        elif 'shutdown' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')
                 
        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")
        
        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20, 
                                                       0, 
                                                       "Location of wallpaper",
                                                       0)
            speak("Background changed succesfully")

        elif 'cmd' or 'command prompt' in query:
            os.startfile("cmd")

        elif 'task manager' in query:
            pyautogui.hotkey('ctrl','shift','esc')
            
        elif 'screenshot' in query:
            pyautogui.hotkey('win','shift','s')
        
        
        
        elif 'search' in query or 'play' in query:
             
            query = query.replace("search", "") 
            query = query.replace("play", "")          
            webbrowser.open(query)
        