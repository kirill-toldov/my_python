trantab = str.maketrans("", "", ".,?-;:!")
words=[]

with open('moby.txt','r') as file:
    for line in file:
        line=line.translate(trantab)
        line=line.lower()
        words+=line.split()

with open('moby_clean.txt','w') as file:
    for word in words:
        file.write(word+'\n')
