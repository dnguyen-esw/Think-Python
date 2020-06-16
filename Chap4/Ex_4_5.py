from swampy.TurtleWorld import *
from math import *

def spiral(t,n,length=3,a=0.1,b=0.0002):
    theta=0.0
    for i in range(n):
        fd(t, length)
        dtheta=1/(a+b*theta)
        lt(t, theta)
        theta+=dtheta

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.001
spiral(bob, n=1000)

wait_for_user()