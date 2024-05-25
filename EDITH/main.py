import os
import pygame
import speech_recognition as sr
#from botdata import *
import pyautogui 
import pywhatkit
from datetime import datetime

from aifunctions.emailbyai import send_email
from  aifunctions.bolo import speak
from  aifunctions.suno import take_command
import speech_recognition as sr



speak("hello sachin good morning how can i help you ")

     
smart_mode = False       


#click_on_chat_button()

while True:
    query = take_command().lower()
    print('\n You: '+ query)
    
    if 'open' in query:
        app_name=  query.replace('open', " ")
        speak('opening'+ app_name)
        pyautogui.press('super')
        pyautogui.typewrite(app_name)
        pyautogui.sleep(0.5)
        pyautogui.press('enter')
    elif 'switch tab' in query:
        pyautogui.hotkey('ctrl','tab' ) 
    elif 'close tab' in query :
        pyautogui.hotkey('ctrl','w')
    elif 'close ' in query:
        pyautogui.hotkey('alt','f4')
        speak('misson accomplished') 
    elif 'sleep' in query :
        speak('thank you sir i am going to sleep whenever you need wake up me i love to help you ')
        sleep= True 
        while sleep :
         query =take_command().lower()
        if 'wake up' in query:
           speak('thank you for waking me up sir  ...its '+ current_time + '   now...what we goona do today')
           sleep =False

    
    elif 'play' in query :
        song_name = query.replace('play','')
        speak ('as u say sir. playing' + song_name + '    on youtube ')
        pywhatkit.playonyt(song_name)
    elif 'time ' in query:
       current_time = datetime.now().strftime('%I:%M %p')
       speak( 'its ' + current_time)
    
    elif 'write an email'in query or 'send an email ' in query or 'compose an email' in query:
        speak('sure sir  i will do that for you , to whom i should send the mail , please provide me with the email')
        speak('.....please input the mail id of the reciver below')
        receiver = input("enter the reciver email address  ::    ")
        speak("sir... kindly tell me the subject of the mail")
        subject = take_command()
        print(subject)
        speak('what should be the context of email')
        email_prompt= take_command()
        content= ("write a email for"+ email_prompt)
        send_email(receiver,subject,content)
        speak('Sir , i have sent the email you asked for .....is there anything else i can do for you ')
        
''' 
        # Handle basic interactions directly
    elif "hello" in query or "heey" in query:
        speak("Hey, how you doing?")
    elif "cool" in query or "fine" in query:
        speak("That's nice to hear!")
        
    elif "what s up" in query or "how are you ":
        speak("I'm doing good. What's your plan for today?")
    elif "thank" in query:
        speak("You're welcome!")
    elif "help" in query:
        speak("Sure, I can help you with this just like your best friend.")
    elif "who are you" in query or"your name" in query:
        speak("Myself Gwen Stacy, I'm an AI model here to help you out.")
    elif "morning" in query:
        speak("Good morning sir! What are we going to do today?")
    elif "later" in query:
        speak("OK sir, I'll wait for it.")
    

    
'''

    
