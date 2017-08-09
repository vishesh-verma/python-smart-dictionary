import json
from difflib import SequenceMatcher

data=json.load(open("data.json",'r'))
def cor():
     for i in data:
               if(SequenceMatcher(None,word,i).ratio()>=.86):
                    return ("did u mean " + i +"?" )


def dec(w):
     if w in data:
        return (data[w][0])

     else:
         return cor()

wor=input("input data: ")
word=wor.lower()
print(" meaning: "  + str(dec(word)))
