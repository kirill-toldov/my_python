class Cat:
    def __init__(self,new_name='Кошка без имени'):
        self._name=new_name
        self._energy=1
        print("Новая кошка",new_name)

    def set_name(self, new_name):
        self._name = new_name

    def get_name(self):
        return self._name

    def eating(self):
        self._energy+=1
        print("Произошло кормление")

    def game(self):
        if self._energy:
            self._energy-=1
            print("Произошла игра с кошкой")
            if not self._energy:
                print('Силы на исходе')
                
        else:
            print("Покормите меня")

    def meow(self):
        if self._energy:
            print("Весёлый мяу")
        else:
            print("Грустный мяу")


my_сat2 = Cat('Барсик')
my_сat2.game()
