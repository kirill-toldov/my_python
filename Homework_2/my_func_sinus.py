'''Упражнение 3.2 (3 балла из 10)
Написать программу, вычисляющую значение функции (на вход
подается вещественное число):
(ответ в виде файла с именем: my_func_sinus.py)'''

from math import sin
 
def my_func_sinus(x):
    if 0.2<=x<=0.9:
        return sin(x)
    else:
        return 1

print(my_func_sinus(float(input('Введите число:\n'))))
