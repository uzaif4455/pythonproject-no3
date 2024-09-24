import googletrans
import speech_recognition
import gtts
import pyaudio

recognizer=speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("Speak Now")
    voice=recognizer.listen(source)
    text=recognizer.recognize_google(voice, language="en")
    print(text)
translator = googletrans.Translator()
translation = translator.translate(text,dest="fr")
print(translation)
