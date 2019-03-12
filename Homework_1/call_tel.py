table={343:15,
       381:18,
       473:13,
       485:11}

def call_tel(code,time):
    if code in table:
        return table[code]*time
    else:
        return 'Данного кода города нет в каталоге.'

print(call_tel(int(input('Введите код города: ')),int(input('Введите время разговора: '))))
