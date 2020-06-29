def find(word, letter, thirdparam):
    index = thirdparam
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

print(find('asdasd','s',2))