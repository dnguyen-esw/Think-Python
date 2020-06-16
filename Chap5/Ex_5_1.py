def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s,n-1)

if __name__ == "__main__":
    pass
print_n('Hello',2)

"""Stack diagram
    <module>    __main__
    print_n     n->2 
    print_n     n->1 
    print_n     n->0 
"""
