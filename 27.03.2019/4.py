def money_reader(what,when):
    """
    Функция возвращает некоторый показатель по сведениям Сбербанка в выбранном городе за указанный период.
    what - что ищем, например 'Средняя зарплата'.
    where - где ищем, например 'Санкт-Петербург'.
    when - когда ищем, указываем год.
    
    """
    import csv
    max_count=0
    region='Ничего не найдено.'
    m=0
    temp_sum=0
    try:
        with open('opendata.csv', encoding='cp1251') as csvfile:
            money_reader = csv.reader(csvfile) # delimiter по умолчанию ','
            for row in money_reader:
                if row[0]==what and row[1]!='Россия' and row[2].split('-')[0]==str(when):
                    if m<12:
                        temp_sum+=int(row[3])
                        m+=1
                    else:
                        print(row[1],temp_sum)
                        if temp_sum>max_count:
                            max_count=temp_sum
                            region=row[1]
                        m=0
                        temp_sum=0
        return region
    except Exception as e:
        return e

if __name__ == '__main__':

  print(money_reader('Количество заявок на потребительские кредиты',2013))
