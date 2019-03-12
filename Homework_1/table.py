table={3:'Li',
       25:'Mn',
       80:'Hg',
       17:'Cl'}

def element_by_number(num):
    if num in table:
        return table[num]
    else:
        return 'Элемента с данным номером нет в каталоге.'        

print(element_by_number(int(input('Введите номер элемента: '))))
