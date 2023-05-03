import pyttsx3 as p
import speech_recognition as sr



engine = p.init()
rate=engine.getProperty('rate')
engine.setProperty('rate',130)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.say("hello there i am your voice assistant juplex")
engine.runAndWait()

r = sr.Recogniser()

with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening")
    audio = r.listen(source)
    text=r.recognise_google(audio)
    print(text)
