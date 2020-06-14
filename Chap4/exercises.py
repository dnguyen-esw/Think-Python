from swampy.TurtleWorld import *
from math import *
world=TurtleWorld()
bob=Turtle()
bob.delay=0.001
#1
def square1(t):
    for i in range(4):
        fd(t,100)
        lt(t)
#square1(bob)

#2
def square2(t, length):
    for i in range(4):
        fd(t, length)
        lt(t)
#square2(bob,200)

#3
def polygon(t,n,length):
    for i in range(n):
        fd(t,length)
        lt(t,360/n)
#polygon(bob,50,10)

#4
def circle(t,r):
    circumference = 2*r*pi
    n = 100
    length = circumference/n
    polygon(t,n,length)    
#circle(bob,50)

def arc(t,r,angle):
    arc_length = 2*pi*r*angle/360
    n = int(arc_length/3)+1
    step_length=arc_length/n
    step_angle=float(angle)/n

    for i in range(n):
        fd(t, step_length)
        lt(t, step_angle)
arc(bob,70,90)

wait_for_user()
