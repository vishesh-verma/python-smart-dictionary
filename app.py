import json
from difflib import get_close_matches

data=json.load(open("data.json",'r'))

def dec(w):
  b=get_close_matches(w,data.keys())

  if w in data:
              return (data[w][0])
  elif(len(b)>0):
       return("did u mean " + str(b[0]) +" instead?")            

  else:
         return("The word does not exits")

wor=input("input data: ")
word=wor.lower()

print(" meaning: "  + str(dec(word)))
