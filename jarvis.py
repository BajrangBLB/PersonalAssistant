import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
from tkinter import Tk, Label

class TranslateGUI():
    def __init__(self, master, text):
        self.master = master;
        master.title("Translated Text")

        self.label = Label(master, text)
        self.label.pack()


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning Boss!")
    
    elif hour >= 12 and hour <= 16:
        speak("Good Afternoon Boss!")
    
    else:
        speak("Good Evening Boss!")
    
    speak("What can I do for you?")


def takeCommand():
    """
    This function takes microphone input from the user and gives string output
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recogniting...")
        query = r.recognize_google(audio, None, "en-IN")
        print(f'You said: {query}\n')
    
    except Exception as e:
        print(e)
        print("Say that again, Please...")
        return "None"

    #speak(query)
    #with open("query.txt", "w") as f:
    #   f.append(query, "\n")
    return query
    

def loop():
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Wikipedia Searching...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia...")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'thank you' in query:
            speak("Your Welcome Boss!")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            speak("I am playing some music from your playlist.")
            music_dir = "C:\\Users\\Bajrang Lal Bishnoi\\Music\\Playlists"
            songs = os.listdir(music_dir)
            n_song = random.randint(0, len(songs))
            print(songs)
            os.startfile(os.path.join(music_dir, songs[n_song]))

        elif 'the time' in query:
            timeStr = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'Sir, the time is {timeStr}')

        elif 'open vs' in query:
            speak("opening visual studio")
            codePath = "C:\\Users\\Bajrang Lal Bishnoi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open python ide' in query:
            speak("opening pycharm for you.")
            pycharmPath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.2\\bin\\pycharm64.exe"
            os.startfile(pycharmPath)

        elif 'open file manager' in query:
            speak("Opening file explorer")
            FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')
            os.startfile(FILEBROWSER_PATH)

        elif 'open typing master' in query:
            speak("Opening Typing Master")
            tyMasterPath = "C:\\Program Files (x86)\\TypingMaster10\\tmaster.exe"
            os.startfile(tyMasterPath)

        elif 'open chrome' in query:
            speak("Opening Google Chrome")
            chromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromePath)

        elif 'open word' in query:
            speak("Opening Microsoft Word")
            wordPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Word 2010"
            os.startfile(wordPath)

        elif 'open excel' in query:
            speak("Opening Microsoft Excel")
            excelPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Excel 2010"
            os.startfile(excelPath)

        elif 'open powerpoint' in query:
            speak("Opening Microsoft PowerPoint")
            powerpointPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft PowerPoint 2010"
            os.startfile(powerpointPath)


        elif 'how are you' in query:
            speak("I am fine boss!")
        
        elif 'i love you' in query:
            speak("I am very happy to know that you liked me.")

        elif 'i like you' in query:
            speak("Thank You Boss")

        elif 'what can you do for me' in query:
            speak("I can help in some computer based tasks")
        
        elif 'translate' in query or 'translte' in query:
            root = Tk()
            trnaslate_gui = TranslateGUI(root)
            root.mainloop()

        elif 'exit' in query:
            speak("See you soon boss")
            break

        elif 'quit' in query:
            speak("See you soon boss")
            break


def play_jarvis():
    
    query = takeCommand().lower()

    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        if 'good morning' in query:
            loop()
    
    elif hour >= 12 and hour < 16:
        if 'good afternoon' in query:
            loop()
    
    elif hour >= 16 and hour <= 24:
        if 'good evening' in query:
            loop()
    

if __name__ == '__main__':

    while True: play_jarvis()
    
