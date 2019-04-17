dict0={'собака':'dog','кот':'cat','тщеславный':'vain','одержимость':'obsession','властвовать':'dominate'}

import tkinter
import random

def click():
    if word.get()==dict0[entry.get()]:
         label.config(text='Это я!')
    else:
         label.config(text='Это не я!')

window = tkinter.Tk()

window.title('Игра?')

frame = tkinter.Frame(window, borderwidth=4, relief=tkinter.GROOVE)
frame.pack()

label1 = tkinter.Label(frame,text='Случайное слово:')
label1.pack()

word=tkinter.StringVar()
word.set(random.choice(list(dict0.values())))

label2 = tkinter.Label(frame,text=word.get())
label2.pack()

label3 = tkinter.Label(frame,text='Это кто?')
label3.pack()

entry = tkinter.Entry(frame)
entry.pack()

button = tkinter.Button(frame, text='Это я?', command=click) 
button.pack()

label = tkinter.Label(frame)
label.pack()

button2 = tkinter.Button(frame, text='Выход?', command=window.destroy) 
button2.pack()

window.mainloop()
