# -*- coding: utf-8 -*-
"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical
value for each name, multiply this value
by its alphabetical position in the list to obtain a name score.
For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the
938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""
def loadAlphabeticalValues():
    alphabet = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".lower().replace(" ", "")
    return {letter : i + 1 for i,letter in enumerate(alphabet)}

def loadNames():
    with open("resources/p022_names.txt") as f:
        data = f.read()
        data = data.replace("\"", "")
        names = data.split(",")
    return sorted(names)

def getNameAlphabeticalScore(name):
    score = 0
    for char in name:
        char = char.lower()
        score += alphabeticalValue[char]
    return score

alphabeticalValue = loadAlphabeticalValues()
names = loadNames()
totalScores = 0


for scoreMultiplier, name in enumerate(names,start=1):
    score = getNameAlphabeticalScore(name)
    score = score * scoreMultiplier
    totalScores += score

print totalScores



