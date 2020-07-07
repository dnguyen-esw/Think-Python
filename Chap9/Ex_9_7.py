def is_3_consecutive(word):
    i=0
    count=0
    while i < len(word)-1:
        if word[i]==word[i+1]:
            count+=1
            if count==3:
                return True
            i=i+2
        else:
            i+=1
            count=0
    return False
def check(file):
    for line in file:
        word=line.strip()
        if is_3_consecutive(word)==True:
            print(word)

fin=open('words.txt')
check(fin)