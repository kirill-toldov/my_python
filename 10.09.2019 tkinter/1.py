import tkinter

class Info:
    def __init__(self):

        
        self.main_window = tkinter.Tk()
        
        self.frame1 = tkinter.Frame(self.main_window)
        self.frame2 = tkinter.Frame(self.main_window)

        
        self.value=tkinter.StringVar()
        
        self.label = tkinter.Label(self.frame1,
                   textvariable=self.value,justify=tkinter.LEFT)
        self.label.pack()
        
        self.info_button = tkinter.Button(self.frame2,
                                        text='info!',
                                        command=self.print_text)
        self.info_button.pack(side='left')
        
        self.quit_button = tkinter.Button(self.frame2,
                                          text='Выйти',
                                command=self.main_window.destroy)
        self.quit_button.pack(side='left')
        
        self.frame1.pack()
        self.frame2.pack(side='bottom')
        
        tkinter.mainloop()
        
    def print_text(self):
        self.value.set('Таю, таю, таю на губах\nКак снежинка таю я в твоих руках\nСтаю, стаю, стаю наших птиц\nБоюсь спугнуть\nДвижением ресниц')
    

info = Info()
