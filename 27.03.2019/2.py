words=[]
with open('moby_clean.txt','r') as file:
    for word in file:
        words+=[word[0:-1]]

sorted_words=sorted(list(set(words)),key=lambda q: words.count(q),reverse=True)

print(sorted_words[0:5])
print(sorted_words[-6:-1])
