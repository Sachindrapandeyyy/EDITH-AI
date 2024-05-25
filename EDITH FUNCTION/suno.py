import speech_recognition as sr



def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        
        
        print("i'm listenning...")
        #speak("i'm listenning...") remove comment for listening the promt a
        r.pause_threshold = 0.5
        audio =r.listen(source)

    try:
      
        print("recognizing...")
        #speak('Recoognizing your questions...')
        query = r.recognize_google(audio, language='en-us,hi-IN',)    
    except  Exception as e:
        print (e)
        return "-"
    return query 