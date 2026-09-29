'''
import gtts
from gtts import gTTS
#now we will give txt nd convert to audio
text = " hi good morning"
g = gTTS(text)
#save as audio file
g.save("audio.mp3")

import gtts
from gtts import gTTS
import playsound
import speech_recognition as sr
import uuid
import os
#now we willgive a text and convert to audio
text = "Hello students hope you are learning and enjoying"
g =gTTS (text)
#save as audio file (.mp3)
g.save("audio.mp3")
playsound.playsound('audio.mp3')

#let us make our virtualAssistant to understand what we speak
#speechRecognition (stt)-->pip install SpeechRecognition
'''
import gtts
import uuid
from gtts import gTTS
import playsound
import speech_recognition as sr
from time import ctime #it returns current time
import os
import webbrowser

#first we will make our virtual Assistant to understand what we speak
def listen():
    """SpeechRecognition"""
    #we will make our system to check the microphone as source
    r = sr. Recognizer()
    with sr.Microphone() as source:
        print("now you can start talking")
        audio = r.listen(source,phrase_time_limit = 5)
    #what ever we speak lets store in data
    data = ""
    #now we will give our exception handiling here to avoid any errors
    try:
        data = r.recognize_google(audio,language="en-us")
        print("you said:",data)
    except sr.UnKnownValueError as e:
        print("make sure to speak louder,so it can be heard")
    except sr.RequestError as e:
        print("Request Failed,please chech your internet connections")
    return data
    #text =gTTS(data)
    #text.save('new.mp3')
    #playsound.playsound('new.mp3')
#listen() #needs to have pyaudio-->pip install pyaudio
#separate functions for responding back and virtual assistant actions

def respond(string):
    """responding function to get audio saved and text is spoken back"""
    print(string)
    tts = gTTS(text = string)
    #only modify content without creating new file
    tts.save('speech.mp3')
    name ='speech%s.mp3'%str(uuid.uuid4())
    tts.save(name)
    playsound.playsound(name)
    os.remove(name)
    
#next we will make our virtualassistant to work with given conditions
def va(data):
    """now we will map our coditions"""
    if "hello"in data:
        listening=True
        respond("hey hai good to see you")
    elif "how are you" in data:
        listening= True
        respond("I am good hope you are well")
    elif "what are your plans"in data:
        listening = True
        respond("em ledu chaduvko")
    elif "time" in data:
        listening =True
        respond(ctime())
    elif "open Google" in data:
        listening= True
        url="https://www.google.com"
        webbrowser.open(url)
        print("success")
        respond("done opened")
    elif "locate" in data:
        listening= True
        url = "https://www.google.com/maps/search/"
        webbrowser.open(url+data.replace("locate",""))
        print("located")
        respond("done maps opened")
    elif "stop talking" in data:
        listening=False
        respond("ok cool..")
    try:
        return listening
    except UnboundLocalError:
        print("Mismactched speack correctly")

respond("Hey")
listening = True
while listening:
    data= listen()
    listening= va(data)
