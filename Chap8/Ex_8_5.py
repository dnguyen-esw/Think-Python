def count(string, word):
    if not isinstance(string,str):
        string=str(string)
    if not isinstance(word,str):
        word=str(word)
    count=0
    for letter in string:
        if letter==word:
            count+=1
    print(count)

string=input("Input string: ")
word=input("Input word to count: ")
count(string,word)