def avoids(word, forbidden):
    """Trả về false nếu trong word có bất kỳ 
    chữ bị cấm nào trong chuỗi forbidden
    """
    count=0
    for letter in word:
        if letter in forbidden:
            return False
    return True


def no_contain(string_of_forbidden):
    """Nhập chuỗi các từ bị cấm và đếm số  từ trong 
    list không chứa bất kỳ từ bị cấm nào trong chuỗi
    """
    no_contain_count=0
    for line in fin:
        result = avoids(line.strip(),string_of_forbidden)
        if result==True:
            no_contain_count+=1
    return no_contain_count

fin=open('words.txt')
print(no_contain('aeoui'))

while True:
    word=input("Type word: ")
    if word=='exit':
        break
    forbidden=input("Input forbidden: ")
    if forbidden =='exit':
        break
    print(avoids(word, forbidden))
    
