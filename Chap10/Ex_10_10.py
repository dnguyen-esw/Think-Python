def makeList_1(file):
    newList = []
    for line in file:
        word = line.strip()
        newList.append(word)
    return newList

def makeList_2(file):
    newList = []
    for line in file:
        word = line.strip()
        newList = newList + [word]
    return newList

fin=open("words.txt")
print(makeList_2(fin))
