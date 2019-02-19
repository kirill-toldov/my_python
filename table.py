table={3:'Li',
       25:'Mn',
       80:'Hg',
       17:'Cl'}

def element_by_number(num):
    if num in table:
        return table[num]
    else:
        return 'Ne znayu takogo elementa'        

print(element_by_number(int(input('Vvedite nomer elementa: '))))
