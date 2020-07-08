def remove_duplicates(list_to_unique):
    newList = []
    for i in list_to_unique:
        if i not in newList:
            newList.append(i)
    return newList

listCheck = ["s","a","b","a","s"]
print(remove_duplicates(listCheck))