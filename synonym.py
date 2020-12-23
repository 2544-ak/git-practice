import nltk
nltk.download()
from nltk.corpus import wordnet as wn

def listToString(list):
    str = " "
    
    return(str.join(list))

stemmed = ['give', 'attend']
string = listToString(stemmed)

print(string)
