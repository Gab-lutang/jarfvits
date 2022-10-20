import os
import speech_recognition as sr

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

    while True:

        wake_Up = takecommand()

        if 'wake up' in wake_Up:
            os.startfile('C:/Users/GAB/Desktop/javis/with play in yt.py')

        else:
            print("Nothing")