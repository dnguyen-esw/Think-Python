def uses_only(word, string_of_letters):
    for letter in word:
        if letter not in string_of_letters:
            return False
    return True

def sentence(file):
    count=0
    for line in file:
        if uses_only(line.strip(),'acefhlo') == True:
            count+=1
            print(line.strip())
    return count

        
fin=open('words.txt')
print(sentence(fin))
print(uses_only("hoangduc","xay"))