class Dog:
    def __init__(self,new_name='Собака без имени'):
        self._name=new_name
        print("Новая собака",new_name)

    def set_name(self, new_name):
        self._name = new_name

    def get_name(self):
        return self._name


dog1=Dog("Демид")
dog1.age=19
