from math import *

def square_root(a, x):
    while True:
        y=(x+a/x)/2
        if y==x:
            return y
        x=y
    
def test_square_root(a, x):
    while a<10:
        #print(a,"\t", square_root(a,3)," "*10, sqrt(a) )
        print("%-1s %-18s %-18s %s" %(a, square_root(a,3), sqrt(a), abs(sqrt(a)-square_root(a,3))))
        a+=1
test_square_root(1,2)
        