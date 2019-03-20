def calc(expr):
    '''
    >>> calc("1 2 + 4 * 3 +")
    '15'
    >>> calc("1 2 3 * + 2 -")
    '5'
    '''
    res=[]
    calcDict={'+':res.append(int(res.pop())+int(res.pop())),
              '*':res.append(int(res.pop())*int(res.pop())),
              '-':res.append(-(int(res.pop())-int(res.pop())))}
    for i in expr.split():
        calcDict.setdefault(i,res.append(i))

         if i=='+':
            res.append(int(res.pop())+int(res.pop()))
        elif i=='*':
            res.append(int(res.pop())*int(res.pop()))
        elif i=='-':
            res.append(-(int(res.pop())-int(res.pop())))
        else:
            res.append(i)
       
            

    return str(res[0])

#print(calc("1 2 3 * + 2 -"))

import doctest
doctest.testmod()
