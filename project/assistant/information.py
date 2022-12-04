

def get_person(command):
    wordList = command.split()
    for i in range(0, len(wordList)):
        if i + 3 <= len(wordList) - 1 and wordList[i].lower() == "who" and wordList[i+1] == "is":
            return wordList[i+2] + " " + wordList[i+3]
    
def get_object(command):
    wordList = command.split()
    for i in range(0, len(wordList)):
        if i + 3 <= len(wordList) - 1 and wordList[i].lower() == "what" and wordList[i+1] == "is":
            return wordList[i+2] + " " + wordList[i+3]
        