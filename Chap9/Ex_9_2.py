def has_no_e(file):
    total=0
    count=0
    for line in file:
        word=line.strip()
        total+=1
        if isinstance(word, str):
            word=str(word)

        if word.find('e')==-1:
            print(word)
            count+=1
            
    percentage=(count/total)*100
    print(percentage)
    print(count)
if __name__ == "__main__":
    fin=open('words.txt')
    has_no_e(fin)

