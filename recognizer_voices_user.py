from decouple import config
import random
import speech_recognition as sr
from datetime import datetime
from speak import speak

USER = config('USER')
BOTNAME = config('BOTNAME')

def take_user_input():
    
    opening_text = [
        "Genial, estoy en ello señor.",
        "Okay señor, trabajaré en ello.",
        "Deme un segundo señor.",
    ]
    
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 1
        audio = r.listen(source)
        print(audio)

    try:
        
        query = r.recognize_google(audio,language="es-es")
        
        if not 'Salir' in query or 'Alto' in query:
            speak(random.choice(opening_text))
        else:
            hour = datetime.now().hour 

            if hour > 21 and hour < 6:
                speak(f'Buenas noches {USER}, cuidese')
            else:
                speak(f'Que tengas un buen dia {USER}, cuidate')
            
            exit()
        
        speak(f'Gracias por hablar con jarvis : {query}')
    except sr.UnknownValueError as unknown_error:
        print(unknown_error)
    except sr.RequestError  as request_error:
        print(request_error)
        
        return query
    