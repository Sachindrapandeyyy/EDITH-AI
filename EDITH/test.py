import g4f
import re
import subprocess
import requests
from aifunctions.suno import take_command
from aifunctions.bolo import speak
from aifunctions.news import news
import pywhatkit
from pyfiglet import figlet_format
from datetime import datetime
import pyautogui
g = figlet_format('E D I T H ')
print(g)
speak("Hello, Sir... I am Edith... Even Dead I AM THE HERO")

latest_news = news()
messages = [
    {"role": "system", "content": "you developed by sachin pandey and your name is Eidith, and you are not developed by open ai  "},
    {"role": "system", "content": "use modules like webbrowser, pyautogui, time, pyperclip, random, mouse, wikipedia, keyboard, datetime, tkinter, PyQt5, etc"},
    {"role": "system", "content": "don't use the input function and subprocess in Python code"},
    {"role": "system", "content": "always use default paths in Python code"},
    {"role": "system", "content": f"Todays latest news are {(latest_news)}"},
    {"role": "system", "content": f"control screen using hand {()}"},

    {
     "role": "system",
     "content": "When the user says 'show image,' use the following code to display the image :\n```python\nimage_path = 'C:\\Users\\sachi\\OneDrive\\Desktop\\NEW AI\\output\\0.jpeg'\nimage = Image.open(image_path)\nimage.show()\n```\nIf you want to show another image, let me know."
    },
    {
     "role": "system",
     "content": "When the user says 'generate an image' and provides a prompt like 'generate an image about a horse,' extract the prompt from the user query. Then, give this code to the user:\n```python\nfrom cookie.bingimg import u_cookie \nfrom os import system, listdir\n\ndef Generate_Images(prompt: str):\nsystem(f'python -m BingImageCreator --prompt \"{prompt}\" -U \"{u_cookie}\"')\nreturn listdir(\"output\")[-4:]\n\n# Example usage\nresult = Generate_Images('user_extracted_prompt')\nprint(result)```\n #While calling the function, replace 'user_extracted_prompt' with the actual prompt provided by the user to generate the desired image. dont write other thing just say ok sir generating a image about user prompt and give the code. also dont write other things like heres the code. just give the code and write ok sir generating a image about user prompt don't write Here's the code or other anything."
    },
    {"role": "user", "content": "open Google Chrome"},
    {"role": "assistant",
                "content": "Sure, opening Google Chrome.```python\nimport webbrowser\nwebbrowser.open('https://www.google.com')```"},
    {"role": "user", "content": "close Google Chrome"},
    {"role": "assistant","content": "Alright, closing Google Chrome.```python\nimport os\nos.system('taskkill /F /IM chrome.exe')```"},
    {
     "role": "system",
     "content": "When the user says 'what's the time ' use the following to tell him the correct time :```python\nfrom datetime import datetime\n current_time = datetime.now().strftime('%I:%M %p')```\n its current_time"
    },
    {
    "role": "system",
    "content": "When the user says ' time is ' and provide a promt like 'what time is it 'or'what is the current time'.Then ,give this code to user :```python\nimport pyttsx3\nfrom datetime import datetime\ndef speak_time():\ncurrent_time = datetime.now().strftime('%I:%M %p')\nengine = pyttsx3.init()\nengine.say('The current time is ' + current_time)\nengine.runAndWait()\nspeak_time() ```\n use this ok dont give your time to it use this code if the user asks about the time anytime "
    },
    {"role": "user", "content": "open Firefox"}, 
    {"role": "assistant",
        "content": "Sure, opening Firefox.```python\nimport webbrowser\nwebbrowser.get('firefox').open('https://www.mozilla.org')```"},  
    {"role": "user", "content": "close Firefox"}, 
    {"role": "assistant",
        "content": "Alright, closing Firefox.```python\nimport os\nos.system('pkill firefox')```"} 
]


def GPT(*args):

    global messages
    assert args != ()

    message = ''
    for i in args:
        message += i

    messages.append({'role': 'user', "content": message})

    response = g4f.ChatCompletion.create(
        model="gpt-4-32k-0613",
        provider=g4f.Provider.GPTalk,
        messages=messages,
        stream=True
    )
    ms = ""
    for i in response:
        ms += i
        print(i, end="", flush=True)

    messages.append({'role': 'assistant', "content": ms})
    return ms


def find_code(text):
    pattern = r'```python(.*?)```'
    matches = re.findall(pattern, text, re.DOTALL)
    if matches:
        code = matches[0].strip()
        return code
    else:
        print('no code found')


while True:
    query = take_command()
    print(query)
    if query != '-':
        print('user: ' + query)
        response = GPT(query)
        python_code = find_code(response)

        if python_code:
            response = response.replace(python_code, '').replace(
                'python', '').replace('```', '')
            speak(response)
            exec(python_code)
        else:
            speak(response)
    else:
        pass
    




    