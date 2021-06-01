from tkinter import *


def click(num):
    global op
    op = op + str(num)
    input_text.set(op)


def evaluate():
    global op
    output = str(eval(op))
    input_text.set(output)
    op = output


def clearDisplay():
    global op
    op = ""
    input_text.set(op)


calc = Tk()
calc.title("계산기")
op = ""

input_text = StringVar()
textarea = Entry(calc, font=('large,_font', 15, 'bold'), bg='#FDFF06', width=28, bd=1, justify="right", insertwidth=3,
                 textvariable=input_text).grid(columnspan=5)

bt7 = Button(calc, font=15, command=lambda: click(7), text="7", bd=3, height=1, width=5).grid(row=1, column=0)
bt8 = Button(calc, font=15, command=lambda: click(8), text="8", bd=3, height=1, width=5).grid(row=1, column=1)
bt9 = Button(calc, font=15, command=lambda: click(9), text="9", bd=3, height=1, width=5).grid(row=1, column=2)
div = Button(calc, font=15, command=lambda: click('/'), text="/", bd=3, height=1, width=5).grid(row=1, column=3)
btC = Button(calc, font=15, command=clearDisplay, text="C", bd=3, height=1, width=5).grid(row=1, column=4)

bt4 = Button(calc, font=15, command=lambda: click(4), text="4", bd=3, height=1, width=5).grid(row=2, column=0)
bt5 = Button(calc, font=15, command=lambda: click(5), text="5", bd=3, height=1, width=5).grid(row=2, column=1)
bt6 = Button(calc, font=15, command=lambda: click(6), text="6", bd=3, height=1, width=5).grid(row=2, column=2)
mul = Button(calc, font=15, command=lambda: click('*'), text="*", bd=3, height=1, width=5).grid(row=2, column=3)

bt1 = Button(calc, font=15, command=lambda: click(1), text="1", bd=3, height=1, width=5).grid(row=3, column=0)
bt2 = Button(calc, font=15, command=lambda: click(2), text="2", bd=3, height=1, width=5).grid(row=3, column=1)
bt3 = Button(calc, font=15, command=lambda: click(3), text="3", bd=3, height=1, width=5).grid(row=3, column=2)
sub = Button(calc, font=15, command=lambda: click('-'), text="-", bd=3, height=1, width=5).grid(row=3, column=3)

bt0 = Button(calc, font=15, command=lambda: click(0), text="0", bd=3, height=1, width=5).grid(row=4, column=0)
dot = Button(calc, font=15, command=lambda: click('.'), text=".", bd=3, height=1, width=5).grid(row=4, column=1)
eql = Button(calc, font=15, command=evaluate, text="=", bd=3, height=1, width=5).grid(row=4, column=2)
add = Button(calc, font=15, command=lambda: click('+'), text="+", bd=3, height=1, width=5).grid(row=4, column=3)

empty1 = Button(calc, font=15, text="", bd=4, height=1, width=5).grid(row=2, column=4)
empty2 = Button(calc, font=15, text="", bd=4, height=1, width=5).grid(row=3, column=4)
empty3 = Button(calc, font=15, text="", bd=4, height=1, width=5).grid(row=4, column=4)

calc.mainloop()
