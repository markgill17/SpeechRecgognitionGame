import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()
with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(text)
    except:
        print("Sorry could not recognize what you said")