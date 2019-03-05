from random import randint

def game(letter):
    ans=input('Угадайте букву!\n')
    if ans==letter:
        return 1
    else:
        game(letter)
        

words=['слово1','слово2','слово3','слово4','слово5']

word=words[randint(0,len(words)-1)]

letter_pos=randint(0,len(word)-1)
letter=word[letter_pos]

qword=word[:letter_pos:]+'?'+word[letter_pos+1::]
print(qword)
game(letter)
print('Правильно, ',word,'.',sep='')
