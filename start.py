from tkinter import *

root = Tk()
version = '0.0.1'
root.title(f'Smart Calculator {version}')
# root.iconbitmap('')
root.geometry('300x300')

# TODO sidebar to choose the Calculator template

frame_inpout = Frame(root)

expression = Label(frame_inpout, text='Exp: 3434 + 56 / 5 =', anchor='e', justify=RIGHT)
expression.pack()
entry = Entry(frame_inpout, justify=RIGHT)
entry.pack(side=BOTTOM)
frame_inpout.pack()

frame_keys = Frame(root)
frame_operators = Frame(root)

# button functions
def AddToExp(num):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(num))


def ButtonClear():
    entry.delete(0, END)


def ButtonPlus():
    pass


def ButtonEqual():
    pass



# define buttons
buttons_1 = Button(frame_keys, text="1", padx=40, pady=20, command=lambda: AddToExp(1))
buttons_2 = Button(frame_keys, text="2", padx=40, pady=20, command=lambda: AddToExp(2))
buttons_3 = Button(frame_keys, text="3", padx=40, pady=20, command=lambda: AddToExp(3))
buttons_4 = Button(frame_keys, text="4", padx=40, pady=20, command=lambda: AddToExp(4))
buttons_5 = Button(frame_keys, text="5", padx=40, pady=20, command=lambda: AddToExp(5))
buttons_6 = Button(frame_keys, text="6", padx=40, pady=20, command=lambda: AddToExp(6))
buttons_7 = Button(frame_keys, text="7", padx=40, pady=20, command=lambda: AddToExp(7))
buttons_8 = Button(frame_keys, text="8", padx=40, pady=20, command=lambda: AddToExp(8))
buttons_9 = Button(frame_keys, text="9", padx=40, pady=20, command=lambda: AddToExp(9))
buttons_0 = Button(frame_keys, text="0", padx=40, pady=20, command=lambda: AddToExp(0))
button_plus = Button(frame_operators, text="+", padx=39, pady=20, command=lambda: AddToExp('+'))
button_minus = Button(frame_operators, text="-", padx=39, pady=20, command=lambda: AddToExp('-'))
button_times = Button(frame_operators, text="X", padx=39, pady=20, command=lambda: AddToExp('*'))
button_div = Button(frame_operators, text="/", padx=39, pady=20, command=lambda: AddToExp('/'))
button_equal = Button(frame_keys, text="=", padx=91, pady=20, command=ButtonEqual)
button_clear = Button(frame_keys, text="Clear", padx=79, pady=20, command=ButtonClear)

# render the buttons on the screen
buttons_7.grid(row=0, column=0)
buttons_8.grid(row=0, column=1)
buttons_9.grid(row=0, column=2)
buttons_4.grid(row=1, column=0)
buttons_5.grid(row=1, column=1)
buttons_6.grid(row=1, column=2)
buttons_1.grid(row=2, column=0)
buttons_2.grid(row=2, column=1)
buttons_3.grid(row=2, column=2)
buttons_0.grid(row=4, column=0)

button_div.grid(row=0, column=0)
button_times.grid(row=1, column=0)
button_minus.grid(row=2, column=0)
button_plus.grid(row=3, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_equal.grid(row=5, column=1, columnspan=2)

frame_keys.pack(side=LEFT)
frame_operators.pack(side=RIGHT)


root.mainloop()