import speech_recognition as sr
import datetime
import subprocess
import pywhatkit
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)
recognizer = sr.Recognizer()
def cmd():
    with sr.Microphone() as source:
        print('Clearing background noises..Please wait')
        recognizer.adjust_for_ambient_noise(source,duration = 0.5)
        print('Ask me anything...')
        recordedaudio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(recordedaudio,language='en_US')
        command = command.lower()
        print('Your message:',format(command))
    except Exception as ex:
        print(ex)

    if 'chrome' in command:
        a = 'Opening chrome..'
        engine.say(a)
        engine.runAndWait()
        program = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        subprocess.Popen([program])
    elif 'time' in command:
        time = datetime.now().strftime('%I:%M %p')
        print(time)
        engine.say(time)
        engine.runAndWait()
    elif 'play' in command:
        b = 'Opening Youtube'
        engine.say(b)
        engine.runAndWait()
        pywhatkit.playonyt(command)
