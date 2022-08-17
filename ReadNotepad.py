import pyttsx3
import speech_recognition as sr
import os
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
def Speak(audio):
    print(" ")
    print(f"LIA: {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")
def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone as source:
        print("LIA: Listening....")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source,timeout=8,phrase_time_limit=8)
    try:
        print("LIA: Recognizing...")
        query = r.recognize_google_cloud(audio,language='en-in')
        print(f"User: {query}\n")
    except:
        return ""
    return query.lower()
def ReadNotepad():
    Speak("Tell Me The name .")
    tempname= TakeCommand()
    a = os.listdir("C:\\Users\\DINESH\\Documents\\Custom Office Templates\\LIA\\DataBase\\NotePad")
    for aa in a :
        if ".txt" in aa:
            if tempname in aa:
                b = open("DataBase\\NotePad\\"+aa,"r")
                Speak(b.read())
                
            else:
                Speak("Sorry sir i cannot find the file")
        else:
            Speak("Sorry sir i cannot find the file")
ReadNotepad()