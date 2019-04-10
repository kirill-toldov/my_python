class point:
    def __init__(self,x=0,y=0):
        self._x=x
        self._y=y
        
    def set(self,x=0,y=0):
        self._x=x
        self._y=y
        
    def get(self):
        return(self._x,self._y)

    def __add__(self,point2):
        return point(self._x+point2._x,self._y+point2._y)

    def __str__(self):
        return str(self.get())

    def dist(self,point2):
         return ((self._x - point2._x)**2 + (self._y - point2._y)**2)**0.5
    


p1=point(1,1)
p2=point(4,5)
p3=p1+p2
print(p3)
