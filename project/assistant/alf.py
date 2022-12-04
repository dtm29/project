from ai import AI
import weather as Weather
import pyjokes
import date as Date
import wikipedia
import information

alf = AI()

def joke():
    funny = pyjokes.get_joke()
    print(funny)
    alf.say(funny)

def weather():
    weather = Weather.forecast()
    print(weather)
    alf.say(weather)

def date():
    date = Date.get_date()
    print(date)
    alf.say(date)   


def person():
    person = information.get_person(command)
    wiki = wikipedia.summary(person, sentences = 2)
    print(wiki)
    alf.say(wiki)

def object():
    obj = information.get_object(command)
    wiki_obj = wikipedia.summary(obj, sentences = 2)
    print(wiki_obj)
    alf.say(wiki_obj)



command = ""  
    
while True and command!="goodbye":
    try:
        command = alf.listen()
        command = command.lower()
    except:
        print("oops there was an error")

    print("command was: ", command)

    if command == "alexa":
        alf.say("Hello Boss, What can I do for you ")
    
    if command == "how old are you":
        alf.say("It's a secret he he he")
    
    if command == "alexa I feel very tired and depressed":
        alf.say("All good things are waiting for you, people are always with you, love you. Even Alexa will always love you, silly little master.Fragrant cheeks, fondly")

    if command == "alexa sing me a song":
        alf.say("La la la, lay la la, you are so cute and handsome, i love you so much , oh oh oh")
     
    if command in["what's the weather", "what is the weather", "give me the forecast"]:
        weather()
    if command == "tell me a joke":
        joke()
    if command == "what day is today":
        date()

    if "who is" in command:
        person()
    if "what is" in command:
        object()
       


alf.say("Goodbye, I'm going to sleep now")        