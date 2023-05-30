#loafing 
from math import sqrt, log
from prettytable import PrettyTable
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

#Gathering sentences into lists
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

#Vectorizing texts
counter1 = 0
counter2 = 0
for word in wordBag:
    for text1 in text1Words:
        if word == text1:
            counter1 += 1
    text1Vector.append(counter1)
    counter1 = 0

    for text2 in text2Words:
        if word == text2:
            counter2 += 1
    text2Vector.append(counter2)
    counter2 = 0

#Calculating similarities
vectorDividend = 0
for i in range(len(text1Vector)):
   vectorDividend += text1Vector[i] * text2Vector[i]

text1Divisor = 0
for i in range(len(text1Vector)):
    text1Divisor += text1Vector[i] ** 2

text2Divisor = 0
for i in range(len(text2Vector)):
    text2Divisor += text2Vector[i] ** 2

#Obtaining cosine of vectors
cosine = vectorDividend / (sqrt(text1Divisor) * sqrt(text2Divisor))
if cosine < 0:
    print(cosine , ': Not quite similar')
if cosine >=0 and cosine <0.5:
    print(cosine, ': Somewhat similar')
if cosine > 0.5:
    print(cosine , ': Likely similar')


#TDF-IDF vectorization
tfText1 = []
tfText2 = []


tfCounter1 = 0
for word in wordBag:
    for tfText in text1Words:
        if word == tfText:
            tfCounter1 += 1
    tfText1.append(tfCounter1/ len(text1Words))
    tfCounter1 = 0

tfCounter2 = 0
for word in wordBag:
    for tfText in text2Words:
        if word == tfText:
            tfCounter2 += 1
    tfText2.append(tfCounter2/ len(text2Words))
    tfCounter2 = 0

idfList = []
documentsContainingWord = 0
idf = 0
for word in wordBag:
    if word in text1Words:
        documentsContainingWord += 1
    if word in text2Words:
        documentsContainingWord += 1
    idf = log(len(lines) / (documentsContainingWord + 1)) + 1
    idfList.append(round(idf,9))
    idf = 0
    documentsContainingWord = 0

    
#Computing final vector
tfText1_IDF = []
tfText2_IDF = []
for i in range(0,len(wordBag)):
    tfText1_IDF.append(tfText1[i] * idfList[i])
    
for i in range(0,len(wordBag)):
    tfText2_IDF.append(tfText2[i] * idfList[i])

tfTable = PrettyTable()
tfTable.add_column('Words', wordBag)
tfTable.add_column('TF(text 1)', tfText1)
tfTable.add_column('TF(text 2)', tfText2)
tfTable.add_column('IDF', idfList)
tfTable.add_column('TF(text1 * IDF)', tfText1_IDF)
tfTable.add_column('TF(text2 * IDF)', tfText2_IDF)

print(tfTable)
