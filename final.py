import json
from difflib import get_close_matches

data=json.load(open("data.json",'r'))

def dec(w):
  b=get_close_matches(w,data.keys())

  if w in data:
              return (data[w][0])
  elif(len(b)>0):
          yn=input("Did you mean: " + b[0]+"\n" +" if yes enter y or n if no")
          if yn=="y":
              return(data[b[0]][0])
          else:
              return("the word dosent exist")

  else:
      return("The word does not exits")

wor=str(input("input data: "))
word=wor.lower()

print(" meaning: "  + str(dec(word)))
