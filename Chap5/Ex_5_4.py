#1
def is_triangle(a, b, c):
    if a > b + c or b > a + c or c > a + b:
        print("No")
    else:
        print("Yes")

#2
def prompts():
    a=input("Type a:")
    b=input("Type b:")
    c=input("Type c:")
    is_triangle(int(a), int(b), int(c))


if __name__ == "__main__":
    pass

prompts()

