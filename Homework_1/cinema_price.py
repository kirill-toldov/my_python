"""
Упражнение 2.5 (7 баллов из 10)

Напишите программу для определения стоимости билетов в кино с учетом скидок.

Скидки
При покупке билетов за день до сеанса: скидка 5%.
Вы можете купить билет со скидкой 20%. Для этого нужно собрать. компанию не менее 20 человек.

Порядок действий:
выбрать фильм
выбрать дату (сегодня, завтра)
выбрать время
указать количество билетов
определить стоимость


Исходные данные:
Фильм «Пятница», 
сеансы: 12 часов – 250 руб, 16 – 350 руб, 20 – 450 руб. 
Фильм «Чемпионы», 
сеансы: 10 часов – 250 руб, 13 – 350 руб, 16 – 350 руб. 
Фильм «Пернатая банда», 
сеансы: 10 часов – 350 руб, 14 – 450 руб, 18 – 450 руб. 


Пример выполнения программы: 2/ cinema.log


Можно решить без создания собственных функций.


(ответ в виде файла с именем: cinema_price.py)
"""

#discount_list = [discount1,discount2]
#нужно будет сделать список функций, проверяющих наличие каждой из скидок
#сейчас проблема с разными аргументами

timetable = {'Пятница':{12:250,16:350,20:450},
              'Чемпионы':{10:250,13:350,16:350},
              'Пернатая банда':{10:350,14:350,18:450}
              }
exit_code = -1

def discount1(price,date):
    return price*(1 - 0.05*date)#здесь и далее все константы нужно задать отдельно, вынеся из, непосредственно, формул

def discount2(price,num_of_tickets):
    return price*(1 - 0.2*(num_of_tickets >= 20))#!константа

def exit():
    0/0 #тут будет окончание работы программы про причине нежелания пользователя продолжать вводить данные

def choose_film():#хорошо было бы не заставлять пользователя не печатать название фильма, а дать ему список названий с номерами
    print('Выберите фильм:\n',list(timetable.keys()))
    film=input()
    if film == str(exit_code):
        exit()
    elif film in timetable.keys():
        return film
    else:
        print('Вы где-то допустили ошибку.\nВозможно, проблема в том, что Вы поставили кавычки. Этого делать не нужно.\nПопробуйте, пожалуйста, ещё раз, либо введите -1 для выхода.\n')
        return choose_film()

def choose_date():
    print('Выберите дату:\n0 - сегодня\n1 - завтра')
    date = int(input())#здесь и далее в функциях считывания данных нужно установить нормальную проверку данных, до преобразования введённой строки в числовое значение
    if date == exit_code:
        exit()
    elif date in [0,1]:#!константа
        return date
    else:
        print('Вы где-то допустили ошибку.\nПопробуйте, пожалуйста, ещё раз, либо введите -1 для выхода.\n')
        return choose_date()

def choose_time(film):
    print('Выберите время:',list(timetable[film].keys()))
    time=int(input())#!проверка данных
    if time == exit_code:
        exit()
    elif time in timetable[film].keys():
        return time
    else:
        print('Вы где-то допустили ошибку.\nПопробуйте, пожалуйста, ещё раз, либо введите -1 для выхода.\n')
        return choose_time()

def choose_num_of_tickets():
    print('Укажите количество билетов:')
    num_of_tickets=int(input())#!проверка данных
    if num_of_tickets == exit_code:
        exit()
    elif num_of_tickets >= 0:
        return num_of_tickets
    else:
        print('Вы где-то допустили ошибку.\nПопробуйте, пожалуйста, ещё раз, либо введите -1 для выхода.\n')
        return choose_num_of_tickets()

def cinema_price(film,time,num_of_tickets):
    return timetable[film][time]*num_of_tickets


def main():
    film=choose_film()
    date=choose_date()
    time=choose_time(film)
    num_of_tickets=choose_num_of_tickets()
    price=cinema_price(film,time,num_of_tickets)
    price=discount1(price,date)
    price=discount2(price,num_of_tickets)
    print('Спасибо.\nОбщая стоимость билетов, с учётом скидок, составит ',price)

main()
