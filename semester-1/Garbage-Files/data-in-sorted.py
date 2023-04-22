FILE = open('b.txt', 'r')
splitFile = FILE.read().split()
uniqueWords = []
for words in splitFile:
    if words not in uniqueWords:
        uniqueWords.append(words)
uniqueWords.sort()
FILE.close()
print(uniqueWords)