from tkinter import *
from tkinter import ttk

window = Tk()
window.title('계산기')
window.geometry('350x200')
Label(window, text='입력값').grid(column=0, row=0)
Label(window, text='입력값').grid(column=0, row=1)

res_label = Label(window, text='출력값')
res_label.grid(column=0, row=2)

input1 = Entry(window, width=10)
input2 = Entry(window, width=10)
result = Label(window, width=10, text=0)
input1.grid(column=1, row=0)
input2.grid(column=1, row=1)
result.grid(column=1, row=2)


def add():
    result_text = str(float(input1.get())+float(input2.get()))
    result.configure(text=result_text)


btn_1 = Button(window, text='1', command=lambda: button_pressed('1'))
btn_1.grid(column=0, row=3)
btn_2 = Button(window, text='2', command=None)
btn_2.grid(column=1, row=3)
btn_3 = Button(window, text='3', command=None)
btn_3.grid(column=2, row=3)
btn_4 = Button(window, text='4', command=None)
btn_4.grid(column=0, row=4)
btn_5 = Button(window, text='5', command=None)
btn_5.grid(column=1, row=4)
btn_6 = Button(window, text='6', command=None)
btn_6.grid(column=2, row=4)
btn_7 = Button(window, text='7', command=None)
btn_7.grid(column=0, row=5)
btn_8 = Button(window, text='8', command=None)
btn_8.grid(column=1, row=5)
btn_9 = Button(window, text='9', command=None)
btn_9.grid(column=2, row=5)
btn_0 = Button(window, text='0', command=None)
btn_0.grid(column=0, row=6)
btn_result = Button(window, text='=', command=None)
btn_result.grid(column=2, row=6)
btn_plus = Button(window, text='+', command=add)
btn_plus.grid(column=3, row=3)
btn_minus = Button(window, text='-', command=None)
btn_minus.grid(column=3, row=4)
btn_mult = Button(window, text='*', command=None)
btn_mult.grid(column=3, row=5)
btn_div = Button(window, text='/', command=None)
btn_div.grid(column=3, row=6)

window.mainloop()
