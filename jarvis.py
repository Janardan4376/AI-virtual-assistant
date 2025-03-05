import pyttsx3
import speech_recognition as sr
import random
import webbrowser
import datetime
from plyer import notification
import pyautogui
import wikipedia
import openai_request as ai

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate",150)
#engine.say("i will speak")
#engine.runAndWait()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def command():
    content = " "
    while content == " ":
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

    # recognize speech using Google Speech Recognition
        try:
            content = r.recognize_google(audio, language='en-in')
            print("You Said.........")
            print("command = " + content)
        except Exception as e:
            print("Please try again...")
    
    return content
def main_process():
    while True:
        request = command().lower()
        if "hello" in request:
            speak("Welcome, How can i help you.")
        elif "play music" in request:
            speak("Playing music")
            song = random.randint(1,3)
            if song == 1:
                webbrowser.open("https://www.youtube.com/watch?v=XO8wew38VM8")
            elif song == 2:
                webbrowser.open("https://www.youtube.com/watch?v=KcILIMV-Lig")
            elif song == 3:
                webbrowser.open("https://www.youtube.com/watch?v=KhnVcAC5bIM")
        elif "say time" in request:
            now_time = datetime.datetime.now().strftime("%H:%M")
            speak("Current time is " + str(now_time))
        elif "say date" in request:
            now_time = datetime.datetime.now().strftime("%d:%m")
            speak("Current date is " + str(now_time))
        elif "new task" in request:
            task = request.replace("new task","")
            task = task.strip()
            if task != "":
                speak("Adding task :"+ task)
                with open("todo.txt","a") as file:
                    file.write(task + "\n")
        elif "speak task" in request:
            with open("todo.txt","r") as file:
                speak("work we have to do today is : " + file.read())
        elif "show work" in request:
            with open("todo.txt","r") as file:
                tasks = file.read()
            notification.notify(
                title = "Todays work",
                message = tasks
            )
        elif "open youtube" in request:
            webbrowser.open("www.youtube.com")
        elif "open" in request:
            query = request.replace("open", "")
            pyautogui.press("super")
            pyautogui.typewrite(query)
            pyautogui.sleep(2)
            pyautogui.press("enter")
        elif "wikipedia" in request:
            request = request.replace("jarvis ", "")
            request = request.replace("search wikipedia ", "")
            result = wikipedia.summary(request, sentences=2)
            speak(result)
        elif "search google" in request:
            request = request.replace("jarvis ", "")
            request = request.replace("search google ", "")
            webbrowser.open("https://www.google.com/search?q="+request)
            speak(result)
        elif "ask ai" in request:
            request = request.replace("jarvis ", "")
            request = request.replace("ask ai ", "")

            request = ai.send_request(request)
            print(request)
            speak(request)
        else:
            request = request.replace("jarvis ", "")
            request = ai.send_request(request)
            print(request)
            speak(request)
main_process()