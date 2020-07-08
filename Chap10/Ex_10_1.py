def nested_sum(nested_list):
    total=0
    for nest in nested_list:
        total=total+ sum(nest)
    return total
nest_list=[[2,5],[6,5,6],[3,3]]
print(nested_sum(nest_list))
