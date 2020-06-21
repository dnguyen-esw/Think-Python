def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(str):
    if len(str) <= 1:
        return True
    if first(str) != last(str):
        return False
    return is_palindrome(middle(str))

print(is_palindrome("noasdon"))