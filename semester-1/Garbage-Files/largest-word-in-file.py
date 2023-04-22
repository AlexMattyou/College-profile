FILE = open('a.txt', 'r')
splitFile = FILE.read().split()
largestWords = []
maxLen = len(max(splitFile,key=len))
for words in splitFile:
    if maxLen == len(words):
        largestWords.append(words)
FILE.close()
print(largestWords)