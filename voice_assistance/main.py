import speech_recognition as sr
import pyttsx3
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia


# Transcribes audio to text
def transcriber():
    # Recognizer
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Por favor, hable ahora...")

        # Tiempo de espera
        r.pause_threshold = 0.8

        print('Ya puedes hablar')
        audio = r.listen(source)

        try:
            transcription = r.recognize_google(audio, language="es-es")
            print('Dijiste: ', transcription)
            return transcription
        # If the recognition doesn't understand the audio
        except sr.UnknownValueError:
            print('Ups, no entendí')
            return 'Sigo esperando'
        # If the transcription can't be resolved
        except sr.RequestError:
            print('Ups, no hay servicio')
            return 'Sigo esperando'
        # Other errors
        except:
            print('Ups, algo salió mal')
            return 'Sigo esperando'


# Voice assistant
def talk(message):
    # Start pyttsx2
    engine = pyttsx3.init()
    engine.setProperty('voice', voice1)

    # Say the message
    engine.say(message)
    engine.runAndWait()


def ask_day():

    day = datetime.date.today()
    print(day)

    week_days = day.weekday()
    day_names = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    print(day_names[week_days])

    talk(f'Hoy es {day_names[week_days]}')


def ask_hour():
    hour = datetime.datetime.now()
    talk(f'En este momento son las {hour.hour} horas con {hour.minute} minutos')

# Obtain different voices and languages
# engine = pyttsx3.init()
# for voice in engine.getProperty('voices'):
#     print(voice)
voice1 = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0'
voice2 = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'


def greetings():
    hour = datetime.datetime.now()
    momento = ''
    if hour.hour < 6 or hour.hour > 20:
        momento = 'Buenas noches'
    elif 6 <= hour.hour < 13:
        momento = 'Buenos días'
    else:
        momento = 'Buenas tardes'

    talk(f'{momento}, soy Helena, tu asistente virtual.')


def ask_something():
    # Initial greetings
    greetings()
    start = True

    while start:
        demand = transcriber().lower()
        if 'abrir youtube' in demand:
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir navegador' in demand:
            talk('Claro, estoy en eso.')
            webbrowser.open('https://www.google.es')
            continue
        elif 'qué día es hoy' in demand:
            ask_day()
            continue
        elif 'qué hora es' in demand:
            ask_hour()
            continue
        elif 'busca en wikipedia' in demand:
            talk('Buscando en wikipedia')
            demand = demand.replace('busca en wikipedia', '')
            wikipedia.set_lang('es')
            result = wikipedia.summary(demand, sentences=1)
            talk('Wikipedia dice lo siguiente:')
            talk(result)
            continue
        elif 'busca en internet' in demand:
            talk('Ya mismo estoy en eso.')
            demand = demand.replace('busca en internet', '')
            pywhatkit.search(demand)
            talk('Estoy es lo que he encontrado:')
            continue
        elif 'reproducir' in demand:
            talk('Buena idea, ya comienzo a reproducirlo')
            demand = demand.replace('reproducir', '')
            pywhatkit.playonyt(demand)
            continue
        elif 'broma' in demand:
            talk(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in demand:
            shares = demand.split('de')[-1].strip()
            wallet = {'apple': 'APPL',
                      'amazon': 'AMZN',
                      'google': 'GOOGL'}
            try:
                searched_shares = wallet[shares]
                searched_shares = yf.Ticker(searched_shares)
                real_price = searched_shares.info['regularMarketPreviousClose']
                talk(f'La encontré, el precio de {shares} es: {real_price}')
                continue
            except:
                talk('Lo siento, pero no la he encontrado.')
                continue
        elif 'adiós' in demand:
            talk('Me voy a descansar, cualquier cosa me avisas.')
            start = False


ask_something()

