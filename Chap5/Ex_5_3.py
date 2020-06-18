from math import *

#1
def check_fermat(a, b, c, n):
    if n>2 and (a**n+b**n)==(c**n):
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work.")

#2
def convert():
    a=input("Type a:")
    b=input("Type b:")
    c=input("Type c:")
    n=input("Type n:")
    a=int(a)
    b=int(b)
    c=int(c)
    n=int(n)
    check_fermat(a, b, c, n)



if __name__ == "__main__":
    pass

convert()
