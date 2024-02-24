import pyttsx3
import webbrowser
import datetime
import speech_recognition as sr
import wikipedia
import os
import matplotlib
import smtplib
import psutil
import pyautogui
import pyaudio



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("good morning!")
    elif 12 <= hour < 18:
        speak("good afternoon")
    else:
        speak("good evening") #speak it gives string and speak it

    speak("I am sweety, how are you ketan")

current_index = 10
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        speak(f"You said: {query}")  # Provide feedback using the speak function

    except Exception as e:
        print("Say that again please....")
        return "None"

    return query


if __name__ == "__main__":
    wishme()
    while True:
        query= takecommand().lower() # it convert all in lowercase 
# logic for executing task based on query
        if 'wikipedia' in query:
            speak('searching wikipedia.....')
            query=query.replace("wikipedia","")
            results= wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")  
          
# ... (existing code)
        
        elif 'play music' in query:
               music_dir = "D:\\music"
               songs = os.listdir(music_dir)
               print(songs)
               os.startfile(os.path.join(music_dir, songs[current_index]))

        elif 'next music' in query:
            music_dir = "D:\\music"
            songs = os.listdir(music_dir)

            # Increment the current index to play the next song
            current_index += 1

            # Check if the index is out of bounds, and reset it to 0 if needed
            if current_index >= len(songs):
                current_index = 0

            os.startfile(os.path.join(music_dir, songs[current_index]))

        elif 'repeat music' in query:
            music_dir = "D:\\music"
            songs = os.listdir(music_dir)

            # Decrement the current index to repeat the previous song
            current_index -= 1

            # Check if the index is out of bounds, and set it to the last index if needed
            if current_index < 0:
                current_index = len(songs) - 1

            os.startfile(os.path.join(music_dir, songs[current_index]))       

             
        elif 'the time'in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir ,the time is{strTime}")
            print(strTime) 
            
       
            
        elif 'open vs code' in query:
            codepath="C:\\Users\\ketan bhogal\\OneDrive\\Desktop\\Visual Studio Code.lnk"
            os.startfile(codepath)
            
        elif 'i am fine' in query:
            speak("ok good day ketan") 
            
            
        elif 'thanks' in query:
            speak("welcome")
              
        elif 'open chrome' in query:
            codepath="C:\\Users\\Public\\Desktop\\Google Chrome.lnk"
            os.startfile(codepath)
                          
        elif 'open eclipse' in query:
            codepath="C:\\Users\\ketan bhogal\\OneDrive\\Desktop\\Eclipse IDE for Enterprise Java and Web Developers - 2023-12.lnk"
            os.startfile(codepath)
            

