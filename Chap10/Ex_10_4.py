def middle(list_to_middle):
    del list_to_middle[0]
    del list_to_middle[len(list_to_middle)-1]
    return list_to_middle

list_to_middle = [2, 5, 9, 9, 1, 2]
print(middle(list_to_middle))
