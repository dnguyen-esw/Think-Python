def uses_only(word, string_of_letters):
    for letter in word:
        if letter not in string_of_letters:
            return False
    return True

def uses_all(word, string_of_required):
    for letter in string_of_required:
        if letter not in word:
            return False
    return True
def count_word(file):
    count=0
    for line in file:
        if uses_all(line.strip(),"aeiou")==True:
            count+=1
    return count

fin=open('words.txt')
print(uses_all("hoangduc","duh"))
print(count_word(fin))