def has_duplicates(list_check):
    newList = list_check[:]
    newList.sort()
    for i in range(len(newList)-1):
        if newList[i]==newList[i+1]:
            return True
    return False


listcheck = [2, 5, 7, 3, 1, 2]
print(has_duplicates(listcheck))
