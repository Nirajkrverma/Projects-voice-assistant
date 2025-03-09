import pyttsx3
import pygame
import speech_recognition as sr
import subprocess
from selieum import infow
from yt import Music
from news import News
from weather_module import Weather
from colorama import Fore, Style, init
from datetime import datetime, timedelta, timezone

init(autoreset=True)

weather_assist = Weather(api_key="df0cd29d20828871c0b113925f4d9214")

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

def speak(text):
    """Convert text to speech using pyttsx3."""
    print(f"{Fore.GREEN}[Assistant]: {text}")
    engine.say(text)
    engine.runAndWait()

def open_application(app_name):
    try:
        if app_name.lower() == 'notepad':
            subprocess.Popen(['notepad.exe'])
        elif app_name.lower() == 'calculator':
            subprocess.Popen(['calc.exe'])
        elif app_name.lower() == 'chrome':
            subprocess.Popen(['chrome.exe'])
        else:
            speak(f"Sorry, I don’t know how to open {app_name}.")
    except Exception as e:
        speak(f"An error occurred while opening {app_name}.")
        print(str(e))

def log_action(action):
    print(f"{Fore.GREEN}[Log]: {action}")

def task_completed():
    message = "Task completed. Please press Enter to continue."
    speak(message)
    input(f"{Fore.GREEN}{message}")

def get_ist_time():
    ist_timezone = timezone(timedelta(hours=5, minutes=30))
    return datetime.now(ist_timezone)

def speak_greeting():
    current_time = get_ist_time()
    hour = current_time.hour

    if 5 <= hour < 12:
        greeting = "Good morning"
    elif 12 <= hour < 17:
        greeting = "Good afternoon"
    elif 17 <= hour < 21:
        greeting = "Good evening"
    else:
        greeting = "Hello, it's late night. Hope you had a good day"

    return greeting

# Greeting with Time Awareness
greeting_message = speak_greeting() + ", Sir. I am your voice assistant. How are you today?"
speak(greeting_message)

r = sr.Recognizer()

with sr.Microphone() as source:
    log_action("Listening for initial response from user")
    r.adjust_for_ambient_noise(source, 1.2)
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio).lower()
        print(f"{Fore.GREEN}User said: {text}")
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Could you please repeat?")
        text = ""
    except sr.RequestError:
        speak("Sorry, I'm having trouble connecting to the service.")
        text = ""

if "what about you" in text or "how about you" in text:
    speak("I am doing well, Sir!")

while True:
    speak("Is there anything I can assist you with today?")

    with sr.Microphone() as source:
        log_action("Listening for main command")
        r.adjust_for_ambient_noise(source, 1.2)
        audio = r.listen(source)
        try:
            text2 = r.recognize_google(audio).lower()
            print(f"{Fore.GREEN}User said: {text2}")
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Could you please repeat?")
            continue
        except sr.RequestError:
            speak("Sorry, I'm having trouble connecting to the service.")
            continue

    if 'information' in text2:
        while True:
            speak("You need information related to which topic?")
            with sr.Microphone() as source:
                log_action("Listening for information topic")
                r.adjust_for_ambient_noise(source, 1.2)
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
                try:
                    infor = r.recognize_google(audio)
                    print(f"{Fore.GREEN}Displaying information about {infor} on Wikipedia.")
                    speak(f"Displaying information about {infor} on Wikipedia.")
                    log_action(f"Fetching information for: {infor}")
                    assist = infow()
                    assist.get_info(infor)
                    task_completed()
                    break
                except sr.UnknownValueError:
                    speak("Sorry, you didn’t say anything. Could you please tell me what information you need?")
                except sr.RequestError:
                    speak("Sorry, I'm having trouble connecting to the service.")
                    break

    elif "play" in text2 and "video" in text2:
        while True:
            speak("Which video would you like to play?")
            with sr.Microphone() as source:
                log_action("Listening for video title")
                r.adjust_for_ambient_noise(source, 1.2)
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
                try:
                    vid = r.recognize_google(audio)
                    print(f"{Fore.GREEN}Playing {vid} on YouTube.")
                    speak(f"Playing {vid} on YouTube.")
                    log_action(f"Playing video: {vid}")
                    assist = Music()
                    assist.play(vid)
                    task_completed()
                    break
                except sr.UnknownValueError:
                    speak("Sorry, you didn’t say anything. Could you please tell me which video to play?")
                except sr.RequestError:
                    speak("Sorry, I'm having trouble connecting to the service.")
                    break

    elif "weather" in text2:
        while True:
            speak("For which city would you like the weather information?")
            with sr.Microphone() as source:
                log_action("Listening for city name for weather")
                r.adjust_for_ambient_noise(source, 1.2)
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
                try:
                    city = r.recognize_google(audio)
                    print(f"{Fore.GREEN}Fetching weather information for {city}.")
                    speak(f"Fetching weather information for {city}.")
                    log_action(f"Fetching weather for city: {city}")
                    weather_info = weather_assist.get_weather(city)
                    speak(weather_info)
                    task_completed()
                    break
                except sr.UnknownValueError:
                    speak("Sorry, you didn’t say anything. Could you please tell me the city name?")
                except sr.RequestError:
                    speak("Sorry, I'm having trouble connecting to the service.")
                    break

    elif "news" in text2:
        while True:
            speak("Which news topic would you like to hear about?")
            with sr.Microphone() as source:
                log_action("Listening for news topic")
                r.adjust_for_ambient_noise(source, 1.2)
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
                try:
                    news_topic = r.recognize_google(audio)
                    print(f"{Fore.GREEN}Fetching news about {news_topic}.")
                    speak(f"Fetching news about {news_topic}.")
                    log_action(f"Fetching news for topic: {news_topic}")
                    news_assist = News()
                    news_assist.open_news(news_topic)
                    task_completed()
                    break
                except sr.UnknownValueError:
                    speak("Sorry, you didn’t say anything. Could you please tell me the news topic?")
                except sr.RequestError:
                    speak("Sorry, I'm having trouble connecting to the service.")
                    break

    elif "open" in text2 and "app" in text2:
        while True:
            speak("Which application would you like to open?")
            with sr.Microphone() as source:
                log_action("Listening for application name")
                r.adjust_for_ambient_noise(source, 1.2)
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
                try:
                    app_name = r.recognize_google(audio)
                    print(f"{Fore.GREEN}Opening {app_name}.")
                    speak(f"Opening {app_name}.")
                    log_action(f"Opening application: {app_name}")
                    open_application(app_name)
                    task_completed()
                    break
                except sr.UnknownValueError:
                    speak("Sorry, you didn’t say anything. Could you please tell me which application to open?")
                except sr.RequestError:
                    speak("Sorry, I'm having trouble connecting to the service.")
                    break

    elif 'no' in text2 or 'quit' in text2:
        speak("Goodbye, Sir. Have a great day!")
        break

    else:
        speak("I'm sorry, I didn't understand that. Could you please repeat?")
