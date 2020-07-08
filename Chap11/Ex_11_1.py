def makeDict(words_list):
    newDict = {}
    for word in words_list:
        newDict[word] = 1
    return newDict



def makeList(file):
    newList = []
    for line in file:
        newList.append(line.strip())
    return newList


fin = open("words.txt")
print(makeDict(makeList(fin)))