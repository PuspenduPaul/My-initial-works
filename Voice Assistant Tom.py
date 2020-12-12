import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

engine.say("Hello Sir!")
engine.say("What can I do for you?")
engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("listining.....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'tom' in command:
                command = command.replace('tom', '')
                print(command)

    except:
        pass
    return command


def run_tom():
    command = take_command()
    print(command)

    if 'play' in command:
        song = command.replace('play', '')
        talk('ok, playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        print(time)
        talk('Current time is ' + time)
    elif 'the date' in command:
        date = datetime.datetime.today().strftime('%D')
        print(date)
        talk('Current date is ' + date)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    else:
        talk('Say it again sir')


while True:
    run_tom()
