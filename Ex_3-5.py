#1 write a function that draws a grid
def plus():
    print(('+'+'-'*4)*2+'+')
    
def dash():
    print(('|'+' '*4)*2+'|')

def dash_x2():
    dash()
    dash()

def dash_x4():
    dash_x2()
    dash_x2()

def plus_dash():
    plus()
    dash_x4()

def grid():
    plus_dash()
    plus_dash()
    plus()

grid()

#2: grid 4x4
def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_plus():
    print('+', end='')
def print_dash():
    print('-', end='')
def print_bar():
    print('|', end='')
def print_space():
    print(' ', end='')
def print_end():
    print()
def nothing():
    "do nothing"
