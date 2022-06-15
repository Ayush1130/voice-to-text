import speech_recognition as sr  

# get audio from the microphone                                                                       
r = sr.Recognizer()                                                                                   
with sr.Microphone() as source:                                                                       
    print("Speak:")                                                                                   
    audio = r.listen(source)   

try:
    print(r.recognize_google(audio))
except sr.UnknownValueError:
    print("Error in audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))
