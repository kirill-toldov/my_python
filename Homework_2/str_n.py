'''Упражнение 4.3 (3 балла из 10)
Написать функцию, которая на вход принимает два аргумента: строку (s)
и целочисленное значение (n).
ЕСЛИ длина строки s превышает число n, ТО функция возвращает строку
s в верхнем регистре, ИНАЧЕ возвращается исходная строка s.
(ответ в виде файла с именем: str_n.py)'''

def str_n(s,n):
    if len(s) > n:
        return s.upper()
    else:
        return s

s='abcde'
n=4
print(str_n(s,n))
