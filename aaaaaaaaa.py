class Car:
    def __init__(self,new_brand='00',new_model='00',new_year='00',new_problems=[]):
        self.brand=new_brand
        self.model=new_model
        self.year=new_year
        self.problems=new_problem
        self.price_dict={'Царапины':100,'Двигатель':200,'Бачок потiк':50}
    
    def price(self):
        total=0
        for p in self.problems:
            total+=self.price_dict[p]
        return total
    
        
class Customer:
    def __init__(self,new_name='00',new_adress='00',new_phone='00'):
        self.name=new_name
        self.adress=new_adress
        self.phone=new_phone
        
class Meneger:
    def __init__(self):
    
        
car=Car()
