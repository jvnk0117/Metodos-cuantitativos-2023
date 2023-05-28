#Declaring lists
lines = []
text1Words = []
text2Words = []
wordBag = []
text1Vector = []
text2Vector = []

#Opening text file
with open('Tercer-periodo/text.txt') as textFile:
    for line in textFile:
        lines.append(line.lower())

for words in lines[0].split():
    text1Words.append(words)


for words in lines[1].split():
    text2Words.append(words)

for word in text1Words:
    if word not in wordBag:
        wordBag.append(word)

for word in text2Words:
    if word not in wordBag:
        wordBag.append(word)




print(wordBag)
