def ack(m, n):
    if m == 0:
        value = n + 1
        print(value)
        return value
    elif m > 0 and n == 0:
        value = ack(m-1, 1)
        print(value)
        return value
    elif m>0 and n>0:
        value = ack(m-1, ack(m, n-1))
        print(value)
        return value

if __name__ == "__main__":
    pass

ack(3, 4)
