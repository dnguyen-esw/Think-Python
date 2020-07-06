def is_abecedarian(word):
    previous = word[0]
    for c in word:
        if c<previous:
            return False
        previous=c
    return True

def count(file):
    count=0
    for line in file:
        if is_abecedarian(line.strip()) == True:
            count+=1
    return count

fin=open('words.txt')
print(is_abecedarian("abcdef"))
print(count(fin))