with open('temper.stat.txt','r') as file:
    lst=[]
    for line in file:
        lst+=[float(line.strip())]
    print('макксимальная:',max(lst))
    print('минимальная:',min(lst))
    print('средняя:',sum(lst)/len(lst))
    print('медианная:',sorted(lst)[len(lst)//2])
    print('уникальных:',len(set(lst)))
