
def GCD(a, b):
    if a==0 and b==0:
        return "Invalid parameters"
    elif b==0:
        return a
    else:
        return GCD(b, a%b)
print(GCD(9,15))