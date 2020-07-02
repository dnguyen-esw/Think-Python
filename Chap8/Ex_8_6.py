def count(word, letter):
    result = 0
    startat = 0
    while startat < len(word):
      next_letter_position = find(word, letter, startat)
      if next_letter_position != -1:
        result += 1
        startat = next_letter_position + 1
      else:
        break
    return result
    
def find(word, letter, thirdparam):
    index = thirdparam
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1
print(count('sadsadhxczwqeu','a'))