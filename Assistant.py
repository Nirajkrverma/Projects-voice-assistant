import pyttsx3 as p
import speech_recognition as sr
from selieum import infow   
from yt import Music
from news import News
from weather_module import Weather
weather_assist = Weather(api_key="df0cd29d20828871c0b113925f4d9214")

engine =p.init()
rate=engine.getProperty('rate')
rate=engine.setProperty('rate',190)
voices=engine.getProperty('voices')
voices=engine.setProperty('voices',voices[0].id)
volume=engine.getProperty('volume')
volume=engine.setProperty('volume',5.0)



def speak(text):
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()
speak('hello there ,I am your virtual asisstant. how are you')
with sr.Microphone() as source:
    r.energy_threshold=15000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening.....")
    audio=r.listen(source)
    text=r.recognize_google(audio)
    print(text)
if "what" and "about" and "you" in text:
    speak('I am having a good day  ')
speak('how may i help you')

with sr.Microphone() as source:
    r.energy_threshold=15000
    r.adjust_for_ambient_noise(source,1.2)
    print('listening....')
    audio=r.listen(source)
    text2=r.recognize_google(audio)
    print(text2)

if 'information' in text2:
    speak('You need information related to which topic')

    with sr.Microphone() as source:
        r.energy_threshold =15000
        r.adjust_for_ambient_noise(source, 1.2)
        print('listening....')
        audio = r.listen(source)
        infor = r.recognize_google(audio)

    assist = infow()
    assist.get_info(infor)


elif "play" and "video" in text2:
    speak("you want to play which video ?")
    with sr.Microphone() as source:
        r.energy_threshold = 15000
        r.adjust_for_ambient_noise(source, 1.2)
        print('listening....')
        audio = r.listen(source)
        vid = r.recognize_google(audio)
    print("Playing {} on youtube".format(vid))
    speak("Playing {} on youtube".format(vid))

    assist=Music()
    assist.play(vid)


elif "weather" in text2:
    speak("For which city would you like the weather information?")

    with sr.Microphone() as source:
        r.energy_threshold = 20000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening for city name...")
        audio = r.listen(source)
        city = r.recognize_google(audio)
    print(f"Fetching weather for {city}")
    speak(f"Fetching weather for {city}")

    weather_info = weather_assist.get_weather(city)
    print(weather_info)
    speak(weather_info)


elif "news" in text2:
    (speak("Which news would you like to hear?"))
    with sr.Microphone() as source:
        r.energy_threshold = 15000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening for news topic...")
        audio = r.listen(source)
        news_topic = r.recognize_google(audio)
    print(f"Fetching news  {news_topic}")
    speak(f"Fetching news  {news_topic}")

    news_assist = News()
    news_assist.open_news(news_topic)

input("Press Enter to close the browser...")





