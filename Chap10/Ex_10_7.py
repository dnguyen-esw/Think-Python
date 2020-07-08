def is_anagram(first, second):
    first_list = list(first)
    second_list = list(second)
    temp_1st = first_list[:]
    temp_2nd = second_list[:]
    temp_1st.sort()
    temp_2nd.sort()
    return temp_1st==temp_2nd

first="rail safety"
second="fairy tales"
print(is_anagram(first, second))
print(is_anagram('sad', 'asd zcx'))