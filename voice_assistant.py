import pyttsx3
import datetime as dt
import speech_recognition as sr
from flask import Flask
import webbrowser as wb
tasks=[]
end_time=[]
span_time=[]
order=[]
engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def Hellotell():
    hr=int(dt.datetime.now().hour)
    print(hr)
    if hr>=0 and hr<=12:
        speak("good morning people")
    elif hr>12 and hr<=23:
        speak("good afternoon people")
def scheduler(user_task):
    speak("scheduling your tasks.please tell me your tasks for today")
    user_task = ListenMe()
    while(1):
      if 'done' in user_task:
        return
      else:
        tasks.append(user_task)
        speak("when do you need to complete it? (railway timings)")
        end_time.append(int(ListenMe()))
        speak("how much time does it take?")
        span_time.append(int(ListenMe()))
        speak("next task please")
        user_task=ListenMe()
def Task_Result():
    for i,j in end_time,span_time:
        order.append(i-j)
        sorted(order)
    return order
def ListenMe():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Hearing you :) ....")
        r.pause_threshold=1.5
        r.energy_threshold=90
        audio=r.listen(source)
    try:
        print('recogonising.... ')
        query= r.recognize_google(audio,language="en-in")
        print(f"You: {query}\n")
    except Exception as e:
        print("Can you come again")
        return 'none'
    return query
if __name__=="__main__":
    speak("this is Harry Potter at your service")
    Hellotell()
    while True:
        speak("what help do you need now?")
        content = ListenMe()
        if 'set schedule' in content:
            scheduler(content)
        elif 'not good'or'sad'or'bad'or ' feeling low' in content:
            speak("Relax yourself... things will get better.")
        elif 'stop'in content:
            break
    print(tasks,end_time,span_time)
    for i in order:
        speak((i))