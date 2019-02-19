table={343:15,
       381:18,
       473:13,
       485:11}

def call_tel(code,time):
    if code in table:
        return table[code]*time
    else:
        return 'Net takogo goroda!'

print(call_tel(int(input('Vvedite kod: ')),int(input('Vvedite vremya: '))))
