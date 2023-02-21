import speech_recognition as sr
import pyttsx3

# Define a linguagem do reconhecimento de voz
r = sr.Recognizer()

# Configura a síntese de voz
engine = pyttsx3.init()

def chatbot(text):
    if "olá" in text.lower():
        return "Olá, como posso ajudar?"
    elif "como você está" in text.lower():
        return "Estou bem, obrigado por perguntar. E você?"
    else:
        return "Desculpe, não entendi o que você falou"

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Fale algo: ")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language='pt-BR')
        response = chatbot(text)
        print(response)
        engine.say(response)
        engine.runAndWait()
    except:
        print("Desculpe, não entendi o que você falou")
