import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    '''This function wishes the user as Good Morning , Good evening or Good Afternoon'''
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour < 12:
        speak("Good Morning !!")

    if hour >=12 and hour < 18:
        speak("Good Afternoon !!")
    else:
        speak("Good evening !!")

    speak("I am Jarvis Mam . Please tell how may I help you")

def takeCommand():
    '''This function works as taking microsoft input from the user and returns string output. '''

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio , language='en-in')
        print(f"User said : {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('yashiagrawal68@gmail.com','Kishu$7890')
    server.sendmail('yashiagrawal68@gmail.com',to,content)
    server.close()

# Logic for executing tasks based on queries

if __name__ == '__main__':
    wishMe()

    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia ")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Ths time is {strTime}")
            speak(f"Mam , the time is {strTime}")

        elif 'open pycharm' in query:
            codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.1.2\\bin\\pycharm64.exe"
            os.startfile(codePath)

        elif 'email to yashi' in query:
            try:
                speak("What should I say ?")
                content = takeCommand()
                to = "yashiagrawal68@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent !")

            except Exception as e:
                print(e)
                speak("Sorry my friend yashi , I am not able to sent this email at this time")

        elif 'quit' in query:
            print("Thanku for your time , Mam !!")
            exit()