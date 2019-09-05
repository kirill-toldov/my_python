import random
from math import sqrt

map_size=20
persons_count=50
wizards_count=50
turns_for_draw=20000

class person:
    def __init__(self,new_name='Unnamed man'):
            self._name=new_name
            self._x=random.randint(0,map_size)
            self._y=random.randint(0,map_size)
            self._life=100
            self._gun=gun('started_gun')
            self._score=0
            
    def get_name(self):
        return self._name

    def run(self):
        self._x+=random.randint(-self._gun._speed,self._gun._speed)
        if self._x>map_size:
            self._x=map_size
        elif self._x<0:
            self.x=0
        self._y+=random.randint(-self._gun._speed,self._gun._speed)
        if self._y>map_size:
            self._y=map_size
        elif self._y<0:
            self.y=0
        if self._life<100:
            self._life+=self._gun._hil+self._score

    def fire(self,other):
        other._life-=self._gun._damage+self._score
    def pick(self,new_gun):
        self._gun=new_gun

class wizard(person):
    def run(self):
        self._x=random.randint(0,map_size)
        self._y=random.randint(0,map_size)
        if self._life<100:
            self._life+=self._gun._hil+self._score

class gun:
    def __init__(self,new_name='Unnamed gun',new_damage=2,new_hil=1,new_range=3,new_speed=1):
        self._name=new_name
        self._damage=new_damage
        self._hil=new_hil
        self._range=new_range
        self._speed=new_speed
        self._x=random.randint(0,map_size)
        self._y=random.randint(0,map_size)

def dist(x1,y1,x2,y2):
    return sqrt((x1-x2)**2+(y1-y2)**2)

p=[]
dp=[]
for i in range(persons_count):
    p+=[person('pudge'+str(i))]
for i in range(wizards_count):
    p+=[wizard('puck'+str(i))]

g=[]
for i in range(100):
    g+=[gun('gun'+str(i),random.randint(7,20),random.randint(1,1),random.randint(3,7),random.randint(2,4))]

turn=0
while len(p)>1 and turn<turns_for_draw:
    turn+=1
    p=sorted(p, key=lambda A: random.random())
    for i in p:
        i.run()

        for j in g:
            if dist(i._x,i._y,j._x,j._y)<=i._gun._range:
                i.pick(j)
                g.remove(j)
                    
            
        for j in p:
            if dist(i._x,i._y,j._x,j._y)<=i._gun._range and i!=j:
                i.fire(j)
                if j._life<0:
                    p.remove(j)
                    dp+=[j]
                    i._score+=1

if len(p)>1:
    print('draw')
elif len(p)==1:
    print('winner is ' + p[0]._name+'. his score is '+str(p[0]._score))
else:
    print('Everyone died')

dp+=p
dp=sorted(dp,key=lambda a: -a._score)
for i in dp:
    if i._score>0:
        print(i._name+' '+str(i._score))
    else:
        break
