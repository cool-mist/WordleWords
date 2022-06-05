#!/usr/bin/python3

from datetime import datetime
import re

def parseWord(w):
    x = re.search("([a-z]+)", w)
    return x.group(1).upper()

seed = "2022-01-23"
seedIndex = 219 + 8
seedDate = datetime.strptime(seed, "%Y-%m-%d")
curDate = datetime.today()
deltaDate = curDate - seedDate
delta = deltaDate.days
curWordIndex = delta + seedIndex
prevWordIndex = curWordIndex - 1
nextWordIndex = curWordIndex + 1

print(seedDate)
print(curDate)
print(delta)

with open("words.json") as f:
    words = f.readlines()

prevWord = parseWord(words[prevWordIndex])
curWord = parseWord(words[curWordIndex])
nextWord = parseWord(words[nextWordIndex])

with open("index.html.template", 'r') as f:
    text = f.read()
    text = re.sub('{{prev}}', prevWord, text)
    text = re.sub('{{cur}}', curWord, text)
    text = re.sub('{{next}}', nextWord, text)

with open("index.html", 'w+') as f:
    f.write(text)
