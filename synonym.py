import nltk
nltk.download()
from nltk.corpus import wordnet as wn

def listToString(list):
    str = " "
    
    return(str.join(list))

stemmed = ['give', 'attend']
string = listToString(stemmed)

print(string)

def process_genre(string):
    for genre in string.split(" "):
        result = []
        for syn in wn.synsets(genre):
            for l in syn.lemmas():
                result.append(l.name())
        result = list(dict.fromkeys(result)) 
        #result = listToString(result)
        print(result)

process_genre(string) 
