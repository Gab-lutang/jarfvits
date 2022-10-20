from winsound import PlaySound
from playsound import playsound
import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install SpeechRecognition
import datetime  # pip install DateTime
import os  # pip install os-sys
import sys
import subprocess  # pip install subprocess.run
import webbrowser as wb  # pip install pycopy-webbrowser
import pyautogui  # pip install PyAutoGUI
import wikipedia  # pip install wikipedia
import pyjokes  # pip install pyjokes
from time import sleep
import pywhatkit as xr

engine = pyttsx3.init()  # initialise pyttsx3
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 0-2 range for different voices
voicespeed = 150  # setting speed
engine.setProperty('rate', voicespeed)
chrome_path = '"C:/Program Files/Google/Chrome/Application/chrome.exe" %s'


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-us')
    except Exception as e:
        print(e)
        return "---"
    return query


def time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(time)
    print(time)


def date():
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    speak("the current date is")
    speak(day)
    speak(month)
    speak(year)


def wishme():
    speak("welcome back sir")

    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <= 12:
        speak("Good morning")
    elif hour >= 12 and hour <= 18:
        speak("Good afternoon")
    elif hour >= 18 and hour <= 24:
        speak("Good evening")
    else:
        speak("Good night")

    speak("how can i help u?")


# Open chrome/Website
def open_chrome():
    # url u want to open
    url = 'http://google.com'
    # Windows
    wb.get(chrome_path).open(url)


if __name__ == "__main__":

    # wishme()
    while True:
        query = takecommand().lower()
        print(query)

        if "time" in query:
            time()

        if "date" in query:
            date()

        # Open chrome/Website
        if "jarvis open chrome" in query:
            open_chrome()

        # Wikipedia search
        elif "wikipedia" in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak(result)
            print(result)

        # Chrome search
        elif "search" in query:
            speak("what should i search?")
            chromepath = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"  # location
            search = takecommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")
        
        # Youtube
        elif "youtube" in query:
            speak("Youtube? Coming right up!")
            wb.open('www.youtube.com')
        
        # Facebook
        elif "facebook" in query:
            speak("Alright sir!")
            wb.open('www.facebook.com')

        # Reddit
        elif "reddit" in query:
            playsound('C:/Users/GAB/Desktop/javis/bruh.wav')
            speak("I'll show you the real memes")
            wb.open("www.reddit.com")

        # Twitter
        elif "open twitter" in query:
            playsound('C:/Users/GAB/Desktop/javis/eww.wav')
            speak("oh, this guy wants to be toxic")
            wb.open("www.twitter.com")
            
            
        # Play on Youtube
        elif 'play' in query:
            a ='opening youtube...'
            engine.say(a)
            engine.runAndWait()
            xr.playonyt(query)

        # Launch applications
        elif "open notepad" in query:  # if open notepad in statement
            speak("opening notepad")  # speak
            location = "C:/WINDOWS/system32/notepad.exe"  # location
            notepad = subprocess.Popen(location)  # location of a software you want to open

        elif "close notepad" in query:
            speak("closing notepad")
            notepad.terminate()  # terminate

        elif "open visual studio" in query:
            speak("don't you dare edit me sir")
            location = "c:/Users/GAB/AppData/Local/Programs/Microsoft VS Code/Code.exe"
            VScode = subprocess.Popen(location)

        elif "close visual studio" in query:
            speak("what did you do to me bruv???")
            VScode.terminate()
        
        elif "open steam" in query:
            speak("what? you're still playing after your losestreak?")
            location = "C:/Program Files (x86)/Steam/steam.exe"
            steam = subprocess.Popen(location)

        elif "close steam" in query:
            speak("hahahaha lose streak again?")
            steam.terminate()

        elif "open firefox" in query:
            location = "C:/Program Files/Mozilla Firefox/firefox.exe"
            firefox = subprocess.Popen(location)

        elif "close firefox" in query:
            firefox.terminate()


        # Random jokes
        elif "joke" in query:
            speak(pyjokes.get_jokes())

        # Logout / Shutdown / Restart
        elif "logout" in query:
            speak('logging out in 5 second')
            sleep(5)
            os.system("shutdown - l")

        elif "shutdown" in query:
            speak('shutting down in 5 second')
            sleep(5)
            os.system("shutdown /s /t 1")

        elif "restart" in query:
            speak('initiating restart in 5 second')
            sleep(5)
            os.system("shutdown /r /t 1")

            # <-------------------------Pyautogui  Features--------------------->

        elif "hidden menu" in query:
            speak('ok sir')
            # Win+X: Open the hidden menu
            pyautogui.hotkey('winleft', 'x')

        elif "task manager" in query:
            speak('opening task manager')
            # Ctrl+Shift+Esc: Open the Task Manager
            pyautogui.hotkey('ctrl', 'shift', 'esc')

        elif "task view" in query:
            # Win+Tab: Open the Task view
            pyautogui.hotkey('winleft', 'tab')

        elif "start menu" in query:
            #open  start menu
            pyautogui.hotkey('winleft')

        elif "take screenshot" in query:
            # win+perscr
            pyautogui.hotkey('winleft', 'prtscr')
            speak("done")

            # Take screenshot save in Given location
                   
        elif "take screenshot" in query:
            img = pyautogui.screenshot()
            img.save("D:/screenshot_1.png")  # file mane and location
            speak("Done")
            

        elif "snip" in query:
            pyautogui.hotkey('winleft', 'shift', 's')

        elif "close this app" in query:
            # alt + f4: close this app
            pyautogui.hotkey('alt', 'f4')

        elif "setting" in query:
            # win+i = open setting
            pyautogui.hotkey('winleft', 'i')

        elif "new virtual desktop" in query:
            # Win+Ctrl+D: Add a new virtual desktop
            pyautogui.hotkey('winleft', 'ctrl', 'd')

        elif "switch tab" in query:
            # alt + tab: change tab
            pyautogui.hotkey('alt', 'tab')
            speak("hmmm...")

        # Jokes
        

        # quit to end the program
        elif "offline" in query:  
            speak("going offline")
            quit()