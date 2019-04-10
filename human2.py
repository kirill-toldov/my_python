from random import randint

class Human:
    def __init__(self,new_name='Иван'):
        self._name=new_name
        self._hunger=-10
        self._energy=-10
        self._motivation=-10
        self._age=0
        self._alive="старости"
        #print(self._name,"родился.")

    def eating(self):
        self._hunger+=randint(1,5)
        #print(self._name,"поел.")

    def sleeping(self):
        self._energy+=randint(1,5)
       #print(self._name,"поспал.")

    def working(self):
        if 65>self._age>=18:
            self._hunger-=randint(1,6)
            self._energy-=randint(1,6)
            self._motivation-=randint(1,6)
            #print(self._name,"поработал.")
        
    def relaxing(self):
        self._motivation+=randint(1,5)
        #print(self._name,"расслабился.")

    def growing(self):
        self._age+=1
        #print("Произошёл день",self._age,"рождения.")

    def alive(self):
        if randint(1,100)<=self._age*1-self._hunger:
            self._alive = "голода"
        elif randint(1,100)<=self._age*1-self._energy:
            self._alive ="переутомления"
        elif randint(1,100)<=self._age*1-self._motivation:
            self._alive ="депрессии"


class Life:
    def life(self, human, years=70):
        while years and human._alive=="старости":
            human.growing()
            human.eating()
            human.sleeping()
            human.working()
            human.relaxing()
            human.alive()
            years -= 1
        
        print(human._name,"умер от",human._alive,"в",human._age,"лет.")

names=["Кирилл","Сергей","Владислав"]
for i in names:
    man=Human(i)
    life_man = Life()
    life_man.life(man)
