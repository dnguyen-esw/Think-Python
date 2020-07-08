
def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res

def capitalize_nested(list_string):
    result=[]
    for s in list_string:
        result.append(capitalize_all(s))
    return result





list_of_string = [['hi'],['okee','hello','what'],['thanks','christmas']]
print(capitalize_nested(list_of_string))