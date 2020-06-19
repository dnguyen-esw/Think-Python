
def is_between(x, y, z):
    if x<=y and y<=z:
        return True
    else:
        return False

if __name__ == "__main__":
    pass

if is_between(5, 3, 4):
    print("True")
elif ~is_between(2, 3, 1):
    print("False")


