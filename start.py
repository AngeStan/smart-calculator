from tkinter import *

root = Tk()
version = '0.0.1'
root.title(f'Smart Calculator {version}')
# root.iconbitmap('')
root.geometry('300x300')

frame_input = Frame(root)
frame_keys = Frame(root)
frame_operators = Frame(root)

label_expression = Label(frame_input, anchor='e', justify=RIGHT)
label_expression.pack()
entry = Entry(frame_input, justify=RIGHT)
entry.pack(side=BOTTOM)
frame_input.pack()

# button functions
def AddToExp(num):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(num))


def ButtonClear():
    entry.delete(0, END)



def ButtonEqual():
    label_expression.configure(text=entry.get())
    result = eval(entry.get())
    entry.delete(0, END)
    entry.insert(0, result)


# define buttons
buttons_1 = Button(frame_keys, text="1", padx=10, pady=10, command=lambda: AddToExp(1))
buttons_2 = Button(frame_keys, text="2", padx=10, pady=10, command=lambda: AddToExp(2))
buttons_3 = Button(frame_keys, text="3", padx=10, pady=10, command=lambda: AddToExp(3))
buttons_4 = Button(frame_keys, text="4", padx=10, pady=10, command=lambda: AddToExp(4))
buttons_5 = Button(frame_keys, text="5", padx=10, pady=10, command=lambda: AddToExp(5))
buttons_6 = Button(frame_keys, text="6", padx=10, pady=10, command=lambda: AddToExp(6))
buttons_7 = Button(frame_keys, text="7", padx=10, pady=10, command=lambda: AddToExp(7))
buttons_8 = Button(frame_keys, text="8", padx=10, pady=10, command=lambda: AddToExp(8))
buttons_9 = Button(frame_keys, text="9", padx=10, pady=10, command=lambda: AddToExp(9))
buttons_0 = Button(frame_keys, text="0", padx=10, pady=10, command=lambda: AddToExp(0))
button_plus = Button(frame_operators, text="+", padx=10, pady=10, command=lambda: AddToExp('+'))
button_minus = Button(frame_operators, text="-", padx=10, pady=10, command=lambda: AddToExp('-'))
button_times = Button(frame_operators, text="X", padx=10, pady=10, command=lambda: AddToExp('*'))
button_div = Button(frame_operators, text="/", padx=10, pady=10, command=lambda: AddToExp('/'))
button_equal = Button(frame_operators, text="=", padx=10, pady=10, command=ButtonEqual)
button_clear = Button(frame_keys, text="Clear", padx=10, pady=10, command=ButtonClear)

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
# button_clear.grid(row=4, column=1, columnspan=2)
button_equal.grid(row=4, column=0)

frame_keys.pack(side=LEFT)
frame_operators.pack(side=LEFT)


root.mainloop()