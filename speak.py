import pyttsx3
from datetime import datetime
from decouple import config

USER = config('USER')
BOTNAME = config('BOTNAME')

engine = pyttsx3.init('sapi5')

# Rate
rate = engine.getProperty('rate')
engine.setProperty('rate',150)
# Volume
volume = engine.getProperty('volume')
engine.setProperty('volume',1.0)
# Voice
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet_user():
    
    hour = datetime.now().hour
    
    if hour >= 0 and hour < 6:
        speak(f'Buenos dias de madrugada {USER}')
    elif hour >= 6 and hour < 12:
        speak(f'Buenos dias {USER}')
    elif hour >= 12 and hour <= 18:
        speak(f'Buenas tardes {USER}')
    else:
        speak(f'Buenas noches {USER}')
    
    speak(f'Yo soy {BOTNAME}, para mí es un placer saludarte')
    speak('¿Cómo puedo asistirte?')
