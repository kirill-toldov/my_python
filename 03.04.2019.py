def to_dict_format(s):
    '''Возвращает целое число, если перевод строки в него представляется возможным.
    В противном случае, возвращает исходную строку с удалёнными пробелами в начале и конце.'''
    s=s.strip()
    if s.isdigit():
        return int(s)
    else:
        return s

def csv_read(file_name):
    '''Возвращает список словарей, интерпретируя первую строку файла (name, address, age) как имена ключей,
    а каждую последующую строку как значения этих ключей'''
    import csv
    d=[]
    try:
        with open(file_name, encoding='cp1251') as csvfile:
                csv_read = csv.reader(csvfile)
                keys=[to_dict_format(key) for key in csv_read.__next__()] #список ключей
                keys_count=len(keys) #количество ключей 
                for row in csv_read:
                    d+=[{keys[i]:to_dict_format(row[i]) for i in range(keys_count)}]
                return d
    except Exception as e:
        return e

print(csv_read('input.txt'))
