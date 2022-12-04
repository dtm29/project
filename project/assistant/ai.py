import pyttsx3
import speech_recognition as sr



class AI():
  
    _name = ""
    
    def __init__(self, name = None):
     
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[1].id)
        name = self.voices[1].name
        print(name)
        self.r = sr.Recognizer()
        self.m = sr.Microphone()
        
        print("Listening")
        if name is not None:
            self._name = name
        with self.m as src:
            self.r.adjust_for_ambient_noise(src)
    
    def say(self, sentence):
        self.engine.say(sentence)
        self.engine.runAndWait()

    def listen(self):
        print("Say something")
        with self.m as src:
            audio = self.r.listen(src)
        print("Got it")
        phrase = ""
        try:
            phrase =  self.r.recognize_google(audio) 
            sentence = "Got it , You said: " + phrase
            self.engine.say(sentence)
            self.engine.runAndWait()
        except Exception as e:
            print("Sorry, didn't catch that")
            self.engine.say("Sorry, din't catch that")
            self.engine.runAndWait()
        print("You said: ", phrase)
        return phrase
     



