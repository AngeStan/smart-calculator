from tkinter import *

root = Tk()
version = '0.0.1'
root.title(f'Smart Calculator {version}')
# root.iconbitmap('')
root.geometry('300x300')

# TODO sidebar to choose the Calculator template

standard = Frame(root)

expression = Label(standard, text='Exp: 3434 + 56 / 5 =', anchor='e', borderwidth=3)
expression.grid(row=0, column=0)
entry = Entry(standard, justify=RIGHT)
entry.grid(row=1, column=0)





standard.pack()
root.mainloop()