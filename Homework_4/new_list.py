def sqrt1(q):
    res=[]
    for i in q:
        res+=[i**(1/2)]
    return res

def sqrt2(q):
    return list(map((lambda x:x**(1/2)),q))

def sqrt3(q):
    return [i**(1/2) for i in q]

testList=[2, 4, 9, 16, 25]

print(sqrt1(testList))
print(sqrt2(testList))
print(sqrt3(testList))
