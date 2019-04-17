import tkinter

window=tkinter.Tk()

label = tkinter.Label(window, text = "Текст.")
label.pack()
label1 = tkinter.Label(window, text = "Ещё текст!")
label1.pack()

frame = tkinter.Frame(window)
frame.pack()
frame2 = tkinter.Frame(window, borderwidth=4, relief=tkinter.GROOVE)
frame2.pack()
first = tkinter.Label(frame2, text='First label')
first.pack()
second = tkinter.Label(frame, text='Second label')
second.pack()
third = tkinter.Label(frame2, text='Third label')
third.pack()

data = tkinter.StringVar()
data.set('Данные в окне')

label = tkinter.Label(window, textvariable=data)
label.pack()

var = tkinter.StringVar()
label = tkinter.Label(frame2, textvariable=var)
label.pack()
entry = tkinter.Entry(frame2, textvariable=var)
entry.pack()

window.mainloop()
