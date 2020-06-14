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

def one_four_one(f,g,h):
    f()
    do_four(g)
    h()

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

def print_1beam():
    one_four_one(nothing,print_dash,print_plus)
def print_1post():
    one_four_one(nothing,print_space,print_bar)

def print_4beam():
    one_four_one(print_plus,print_1beam,print_end)
def print_4post():
    one_four_one(print_bar,print_1post,print_end)
def print_row():
    one_four_one(nothing,print_4post,print_4beam)
def print_grid():
    one_four_one(print_4beam,print_row,print_end)
print_grid()
