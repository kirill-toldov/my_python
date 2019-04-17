import tkinter
import cel_to_far

def is_digit(string):
    if string.isdigit():
       return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False

def click():
    if is_digit(entry.get()):
        label.config(text=cel_to_far.celc_to_far(float(entry.get())))
    else:
         label.config(text='Ошибка!')
        

window = tkinter.Tk()

window.title('Конвертировать?')

frame = tkinter.Frame(window, borderwidth=4, relief=tkinter.GROOVE)
frame.pack()

entry = tkinter.Entry(frame)
entry.pack()

label = tkinter.Label(frame)
label.pack()

button = tkinter.Button(frame, text='Это кто?', command=click) 
button.pack()

button2 = tkinter.Button(frame, text='Выход?', command=window.destroy) 
button2.pack()

window.mainloop()
