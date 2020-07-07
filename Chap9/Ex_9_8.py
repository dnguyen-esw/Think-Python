
def is_palindrome(number, start, leng):
    s=str(number)[start:start+leng]
    return s[::-1]==s

def check_palindrome(number):
    return (is_palindrome(number, 2, 4) and is_palindrome(number+1, 1, 5) and is_palindrome(number+2, 1, 4) and is_palindrome(number+3, 0, 6))

def check_all():
    for i in range(100000,999999):
        if check_palindrome(i):
            print(i)

check_all()