import pprint
from oxford import Word
import pandas as pd
import json

path = "C:/Users/twang/Desktop/oxford.json"

# run: multiple namespaces
# loud: no namespace
Word.get('run')

pprint.pprint(Word.info())

# pprint.pprint(Word.id())
# pprint.pprint(Word.name())
# pprint.pprint(Word.wordform())
# pprint.pprint(Word.pronunciations())
# pprint.pprint(Word.definitions())
# pprint.pprint(Word.examples())
# pprint.pprint(Word.definitions(full=True))
# pprint.pprint(Word.idioms())
# pprint.pprint(Word.other_results())

# opening the file in read mode
my_file = open(r"G:\My Drive\PROJECTS_WORK\DICTS\EN-XX\Oxford 5000.txt", "r")
  
# reading the file
data = my_file.read()
  
# replacing end of line('/n') with ' ' and
# splitting the text it further when '.' is seen.
content = data.split("\n")
my_file.close()

k = 0

for i in range(0,len(content)):
    try:
        Word.get(content[i])
        d[content[i]] = Word.info()
        print(str(i),"/",str(len(content)),"found:",content[i])
        k += 1
    except:
        print(str(i),"/",str(len(content)),"not found found:",content[i])
        pass
    if k == 100:
        with open(path, "w") as outfile:
            json.dump(d, outfile)
        print("saving...")
        k = 0


