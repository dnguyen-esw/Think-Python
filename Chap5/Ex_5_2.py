def print_hello():
    print("hello")

def do_n(f,n):
    if n<=0:
        return
    else:
        f()
        do_n(f,n-1)

if __name__ == "__main__":
    pass

do_n(print_hello,5)


