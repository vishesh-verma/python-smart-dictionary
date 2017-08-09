import json
from difflib import get_close_matches

data=json.load(open("data.json",))

def dec(w):

  w=w.lower()
  if w in data:
              return (data[w][0])
  elif len(get_close_matches(w, data.keys())) >0:

        return "did u mean %s instead?" % get_close_matches(w, data.keys())[0]
  else:
         return("The word does not exits")

word=str(input("input data: "))


print(dec(word))
