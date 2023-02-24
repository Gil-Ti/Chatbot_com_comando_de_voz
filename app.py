from flask import Flask, render_template, request
import speech_recognition as sr
import pyttsx3
import nltk
from nltk.chat.util import Chat, reflections

app = Flask(__name__)
pairs = [
    # Exemplo de regra para o chatbot
    ('oi', ['Olá!', 'Oi!', 'Tudo bem?']),
    ('tchau', ['Tchau!', 'Até mais!', 'Foi bom falar com você.']),
]
chatbot = Chat(pairs, reflections)
r = sr.Recognizer()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/voice_input', methods=['POST'])
def voice_input():
    with sr.Microphone() as source:
        print("Diga algo...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language='pt-BR')
    except sr.UnknownValueError:
        text = "Desculpe, não consegui entender o que você disse."
    except sr.RequestError:
        text = "Desculpe, ocorreu um erro no reconhecimento de fala."

    response = chatbot.respond(text)

    with sr.Microphone() as source:
        print(response)
        engine = pyttsx3.init()
        engine.say(response)
        engine.runAndWait()

    return render_template('index.html', text=text, response=response)

if __name__ == '__main__':
    app.run(debug=True)
