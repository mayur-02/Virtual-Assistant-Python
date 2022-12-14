import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Mr.Mayur")

    elif hour>=12 and hour<18:
            speak("Good Afternoon Mr.Mayur")

    else:
                speak("Good Evening Mr.Mayur")
            
    speak("I am MG. Please tell me how may I help you")
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...You Sir")
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say That Again Please...")
        return "None"
    return query

if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...Please Wait")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")


        elif 'play music' in query:
            music_dir = 'F:\Music\Videoder'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[4]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, The Time is {strTime}")

        elif 'open chrome' in query:
            codepath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codepath)
