import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install SpeechRecognition pyaudio
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import sys
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')

def greetings():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print('Good Morning!')
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        print('Good Afternoon!')
        speak("Good Afternoon!")   

    else:
        print('Good Evening!')
        speak("Good Evening!")
    
    print('I am your buddy. Please tell me how may I help you')       
    speak("I am your buddy. Please tell me how may I help you")

def bye():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print('Bye Bye, Have a Good Day.')
        speak("Bye Bye, Have a Good Day.")

    elif hour>=12 and hour<18:
        print('Bye Bye, Enjoy Your Evening.')
        speak("Bye Bye, Enjoy Your Evening.")

    else:
        print('Bye Bye, Good Night')
        speak("Bye Bye, Good Night") 

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
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

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password') # Enter your adress and password
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


if __name__ == "__main__" :
    screen_clear()
    greetings()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open exploit cat' in query:
            webbrowser.open("exploitcat.com")
            
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'play arijit singh' in query:
            webbrowser.open("youtu.be/JK1fPt6gGsE")

        elif 'play punjabi songs' in query:
            webbrowser.open("youtu.be/aOlQhmyog7k")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open blackboard' in query:
            webbrowser.open("cuchd.blackboard.com")

        elif 'open google map' in query:
            webbrowser.open("google.co.in/maps")
        
        elif 'gmail' or 'open gmail' in query:
            webbrowser.open("mail.google.com")

        elif 'shutdown my pc' in query:   
            os.system("shutdown /s /t 1")

        elif 'play music' in query:
            music_dir = 'path' #Give path to file
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "path" #Give path to file
            os.startfile(codePath)

        elif 'open chrome' in query:
            chromePath = "path" #Give path to file
            os.startfile(chromePath)

        elif 'open recyclebeen' in query:
            recyclebeenPath = "path" #Give path to file
            os.startfile(recyclebeenPath)

        elif 'open powershell' in query:
            powershellPath = "path" #Give path to file
            os.startfile(powershellPath)
        
        elif 'exit' in query:
            bye()
            sys.exit()

        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "email@gmail.com"  #change this adress  
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email")