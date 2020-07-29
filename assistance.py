import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot=ChatBot("Jarvis")
tr=ListTrainer(bot)
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate', 150) 
# Set volume 0-1 
engine.setProperty('volume', 0.7)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishing():
    hour = int(datetime.datetime.now().hour)

    if hour >=0 and hour<12:
        speak("Mornin Prassanjt")
    elif hour>=12 and hour<18:
         speak("afternoon Prassanjit")
    else:
        speak("Evening Prassanjit")
    
    speak("Hello. I m your JB, tell me what can i do for you...")

def takecmd():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recogninzing....")
        query = r.recognize_google(audio, language='en-in')
        print("user said : ", query)
    
    except Exception as e:
        print("pardon please.....")
        return "None"

    return query

def sendfile(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.sttls()
    server.login('prassanjitmittal24@gmail.com' , 'iamtoocool')
    server.sendmail('prassanjitmittal24@gmail.com', to, content)
    server.close()
    

if __name__ == "__main__":
    
    wishing()

    while True:



        
        query = takecmd().lower()

             

        if 'wikipedia' in query:
            speak('Searchng wikipedia...')
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query, sentences = 3)
            speak("According to wikipedia ")
            print(results)
            speak(results)
        
        elif 'youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'google' in query:
            webbrowser.open("google.com")
        
        elif 'play music' in query:
            music_dir = 'E:\\audio'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            startTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"this time is {startTime}")

        elif 'code' in query:
            path = "C:\\Users\\acer\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)

        elif 'to pakoda' in query:
            try:
                speak("What should i type....")
                content = takecmd()
                to = "triptimittal15@gmail.com"
                sendfile(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("I m not able to send it")
            

