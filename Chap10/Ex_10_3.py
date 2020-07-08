def cumulative_sum(list_numbers):
    result=[]
    for i in range(len(list_numbers)):
        result.append(sum(list_numbers[:i+1]))
    return result


print(cumulative_sum([1, 2, 3]))