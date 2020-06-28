from math import *
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

def estimate_pi():
    factor=2*sqrt(2)/9801
    total=0
    k=0
    while True:
        summation=(factorial(4*k)*(1103+26390*k))/(pow(factorial(k),4)*pow(396,4*k))
        term=factor*summation
        total+=term
        if abs(term<1e-15):
            break
        k+=1
    return 1/total

print(estimate_pi())
