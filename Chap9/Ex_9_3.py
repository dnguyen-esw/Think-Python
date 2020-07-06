def avoids(word, forbidden):
    for letter in word:
        if letter in forbidden:
            return False
    return True

while True:
    word=input("Type word: ")
    if word=='exit':
        break
    forbidden=input("Input forbidden: ")
    if forbidden =='exit':
        break
    print(avoids(word, forbidden))
    
