import tkinter

class Q:
    def __init__(self):
        
        self.list=['Таю, таю, таю на губах\nКак снежинка таю я в твоих руках\nСтаю, стаю, стаю наших птиц\nБоюсь спугнуть\nДвижением ресниц','Капелькой неба лягу на твою ладонь\nБылью станет небыль, сон исполнится любой\nКапелькою света на ресницы упаду\nИ зимою в лето за собою уведу','Девочкой своею ты меня назови,\nа потом обними,\nа потом обмани,\nА маленькие часики смеются тик-так\nни о чём не жалей\nи люби просто так.']

        
        self.main_window = tkinter.Tk()
        
        self.frame1 = tkinter.Frame(self.main_window)
        self.frame2 = tkinter.Frame(self.main_window)

        
        self.value=tkinter.StringVar()
        
        self.label = tkinter.Label(self.frame1,
                   textvariable=self.value)
        
        self.label.pack()
        
        
        self.button1 = tkinter.Button(self.frame2,
                                        text='таю',
                                        command=self.print_text0)
        self.button2 = tkinter.Button(self.frame2,
                                        text='капелькою неба',
                                        command=self.print_text1)
        self.button3 = tkinter.Button(self.frame2,
                                        text='часики',
                                        command=self.print_text2)
        self.button1.pack(side='left')
        self.button2.pack(side='left')
        self.button3.pack(side='left')
    
        
        self.frame1.pack()
        self.frame2.pack(side='bottom')
        
        tkinter.mainloop()
        
    def print_text0(self):                                    
        self.value.set(self.list[0])
    def print_text1(self):                                    
        self.value.set(self.list[1])
    def print_text2(self):                                    
        self.value.set(self.list[2])
        
             
    

info = Q()
