fruit='banana'
def is_palindrome(string):
    if not isinstance(string, str):
        string=str(string)
    palindrome=string[::-1]
    if string==palindrome:
        return True
    else:
        return False
while True:
    string=input("Input string to check: ")
    if string=='stop':
        break
    print(is_palindrome(string))