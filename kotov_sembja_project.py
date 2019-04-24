import tkinter

def click():
    output_label.config(text=var.get())

window = tkinter.Tk()

frame = tkinter.Frame(window, borderwidth=4, relief=tkinter.GROOVE)
frame.pack()

title_label=tkinter.Label(frame,text='Программа для вычисления объёма сферы.')
title_label.pack()

input_title_label=tkinter.Label(frame,text='Введите радиус:')
input_title_label.pack()

var = tkinter.StringVar()

entry = tkinter.Entry(frame, textvariable=var)
entry.pack()

output_title_label=tkinter.Label(frame,text='Результат вычислений:')
output_title_label.pack()

output_label = tkinter.Label(frame)
output_label.pack()


solve_button = tkinter.Button(frame, text='Вычислить.', command=click) 
solve_button.pack()
