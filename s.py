class StringVar:
    def __init__(self,new_string=""):
        self._string=new_string

    def set(self,new_string=""):
        self._string=new_string

    def get(self):
        return(self._string)

s=StringVar("string")
print(s.get())
s.set()
print(s.get())
