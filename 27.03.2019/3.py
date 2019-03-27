trantab = str.maketrans("", "", '.,?"—;:!*')
max_len=0
max_word=''
with open('test.txt','r') as file:
    for line in file:
        line=line.translate(trantab)
        words=line.split()
        sorted_words=sorted(words,key=lambda q: len(q),reverse=True)
        if len(sorted_words) and len(sorted_words[0])>max_len:
            max_len=len(sorted_words[0])
            max_word=sorted_words[0]
print(max_len,max_word)
