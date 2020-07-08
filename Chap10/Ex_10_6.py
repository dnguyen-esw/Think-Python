def is_sorted(list_to_check):
    temp_list = list_to_check[:]    #make copies to avoid aliasing
    temp_list.sort()
    return (temp_list==list_to_check)

list_check1 = [1, 2, 5, 2, 1]
list_check2 = [1, 2, 3, 4, 7]
#is_sorted(list_check1)
print(is_sorted(list_check1))
print(is_sorted(list_check2))




