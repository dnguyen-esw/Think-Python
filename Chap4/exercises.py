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

#5
def polyline(t, n, length, angle):
    for i in range(n):
        fd(t, length)
        lt(t, angle)
def polygon2(t, n, length):
    angle=360.0/n
    polyline(t, n, length, angle)
def arc(t,r,angle):
    """Draw a circle with a fraction
    """
    arc_length = 2*pi*r*angle/360
    n = int(arc_length/3)+1
    step_length=arc_length/n
    step_angle=float(angle)/n
    polyline(t, n, step_length, step_angle)
def circle2(t, r):
    arc(t, r, 360)

arc(bob,10, 180)
#circle2(bob,20)

wait_for_user()
