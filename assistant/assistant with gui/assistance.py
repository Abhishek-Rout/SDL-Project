from tkinter import *
from PIL import ImageTk,Image
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
from tkinter import messagebox
import mysql.connector as sql
import tkinter


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[2].id')

def speak(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        #r.adjust_for_ambient_noise(source, duration=0.1)
        print("Listening....")
        audio=r.listen(source)
        try:
            print("Recognizing......")
            query=r.recognize_google(audio,language='en-US')
            print(f"User said: {query}\n")
        except Exception as e:
            speak("Say that again please")
            return "None"
        return query

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you") 



class Widget:
    def __init__(self): 
        root=Tk()
        root.title('JARVIS')
        root.configure(bg = "black")
        root.geometry('1366x720')

        img=ImageTk.PhotoImage(Image.open(r"C:\Users\abhis\OneDrive\Desktop\sdl project\assistant code\jarvis.gif"))
        panel=Label(root,image=img,bg="black")
        panel.pack(side='right',fill='both',expand='no')

        self.compText=StringVar()
        self.userText=StringVar()

        self.userText.set('Click Run jarvis to give command')

        userFrame=LabelFrame(root,text="User",font=('Black ops one',10,'bold'),bg="#114B88",fg='white')
        userFrame.pack(fill='both',expand=True)

        left=Message(userFrame,textvariable=self.userText,bg='black',fg='white')
        left.config(font=("Century Gothic",15,"bold"))
        left.pack(fill='both',expand=True)

        compFrame=LabelFrame(root,text='Jarvis',font=('Black ops one',10,'bold'),bg="#114B88",fg='white')
        compFrame.pack(fill='both',expand=True)

        left2=Message(compFrame,textvariable=self.compText,bg='black',fg='white')
        left2.config(font=("Century Gothic",10,"bold"))
        left2.pack(fill='both',expand=True)

        self.compText.set('Hello I am Jarvis what can I do for you sir?')

        btn=Button(root,text='Run Jarvis',font=("Century Gothic",10,"bold"),bg='#4B4B4B',fg='white',command=self.clicked).place(x=1070,y=10)
        btn2=Button(root,text='Close',font=("Century Gothic",10,"bold"),bg='#5A6067',fg='white',command=root.destroy).place(x=1070,y=40)
        #btn2.pack()
       

        root.bind("<Return>",self.clicked)


        root.mainloop()
    
    
    def clicked(self):
        self.userText.set('Listening.....')
        query=takeCommand()
        self.userText.set(query)
        query=query.lower()

       
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            #print(results)
            self.compText.set(results)
            speak(results)

        
        elif 'open youtube' in query:
            webbrowser.open_new_tab("https://www.youtube.com")
            self.compText.set("Youtube is open now")
            speak("youtube is open now")
            time.sleep(2)

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("Google is open now")
            time.sleep(2)

        elif 'open gmail' in query:
                webbrowser.open_new_tab("https://bit.ly/3iOcR5z")
                self.compText.set("Google Mail opening now")
                speak("Google Mail opening now")  
                time.sleep(2)

        elif 'news' in query:
                news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
                speak('Here are some headlines for you')
                time.sleep(2)

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
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                self.compText.set(" Temperature in kelvin unit = " +
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
            self.compText.set(current_time)
            speak(str(current_time.hour)+'hour'+str(current_time.minute)+'minutes')

        elif 'open chrome' in query:
              chromePath = "C:\Program Files (x86)\Google\Chrome\Application\chrome"
              os.startfile(chromePath)
              time.sleep(2)

        elif 'change tab' in query:
              pyautogui.keyDown("alt")
              pyautogui.press("tab")
              pyautogui.keyUp("alt")

        elif 'open calculator' in query:
            subprocess.Popen('C:\\Windows\\System32\\calc.exe')
            time.sleep(2)

        elif 'open notepad' in query:
          subprocess.Popen('C:\\Windows\\System32\\notepad.exe')
          time.sleep(2)

        elif "log off" in query or "sign out" in query:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

        elif "camera" in query or "take a photo" in query or "capture"in query:
            #date_string = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M")
            ec.capture(0,"robo camera","img.jpg")
            time.sleep(2)

        elif 'show all installed apps' in query:             
            for app in winapps.list_installed():
                file.write(app)
                self.compText.set(app+"\n")     
                
                #speak(app)
        
        elif 'search software' in query:
            speak('Which software do you want to search')
            soft=takeCommand()
            for app in winapps.search_installed(soft):
                self.compText.set(app)
        
        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('note.txt', 'w')                
            file.write(note)
         
        elif "show note" in query:
            speak("Showing Notes")
            file = open("note.txt", "r") 
            self.compText.set(file.read())
            speak(file.read(6))

        elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()
 
        elif 'shutdown' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')
                 
        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = True, sound = True)
            speak("Recycle Bin Recycled")
        
        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20, 
                                                       0, 
                                                       "Location of wallpaper",
                                                       0)
            speak("Background changed succesfully")

        

        elif 'task manager' in query:
            pyautogui.hotkey('ctrl','shift','esc')
            time.sleep(2)

        elif 'screenshot' in query:
            pyautogui.hotkey('win','shift','s')
            time.sleep(5)

        
        elif 'search' in query or 'play' in query:
             
            query = query.replace("search", "") 
            query = query.replace("play", "")          
            webbrowser.open(query)
            time.sleep(5)

        
        
        elif 'settings' in query:
             subprocess.Popen([r"C:\\Windows\\System32\\DpiScaling.exe"])

        elif 'device manager' in query:
            subprocess.call("control /name Microsoft.DeviceManager")
        
        elif 'devices' in query:
            os.system('control /name Microsoft.DevicesAndPrinters')
        
        elif 'open pycharm' in query:
            os.startfile("C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.2\\bin\\pycharm64.exe")
        
        elif'open code' in query:
            os.startfile("C:\\Users\\abhis\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
        
        #elif 'cmd' or 'command prompt' in query:
        #    os.startfile("cmd")
        #    time.sleep(2)
        
        #elif 'open drive' or 'open disc' in query:
        #        speak("Which drive you have to open")
        #        statement=takeCommand()
        #        if "C" in statement or "c " in statement: 
         #           os.startfile("C:") 
    

        #        elif "D" in statement or "d" in statement: 
         #           os.startfile("D:") 
  

         #       elif "E" in statement or "e" in statement: 
         #           os.startfile("E:") 
  
         #       else: 
         #           print("Wrong Input")

if __name__=='__main__':
    speak("Initializing Jarvis")
    wishMe()
    widget=Widget()