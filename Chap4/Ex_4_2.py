from swampy.TurtleWorld import *
from math import *
from Ex_4_1 import *

def move(t, length):
    pu(t)
    fd(t, length)
    pd(t)

def petal(t, r, angle):
    """Draws a petal using two arcs.

    t: Turtle
    r: radius of the arcs
    angle: angle (degrees) that subtends the arcs
    """
    for i in range(2):
        arc(t, r, angle)
        lt(t, 180-angle)
def flower(t, n, r, angle):
    """Draws a flower with n petals.

    t: Turtle
    n: number of petals
    r: radius of the arcs
    angle: angle (degrees) that subtends the arcs
    """
    for i in range(n):
        petal(t, r, angle)
        lt(t, 360.0/n)


if __name__ == '__main__':

    world = TurtleWorld()
    bob = Turtle()
    bob.delay = 0.001

    move(bob, -100)
    flower(bob, 7, 60, 60)
    move(bob, 100)
    flower(bob, 10, 40, 80)
    move(bob, 100)
    flower(bob, 20, 140, 20)
    move(bob, 300)
    flower(bob, 50, 100, 360)
    wait_for_user()
    

