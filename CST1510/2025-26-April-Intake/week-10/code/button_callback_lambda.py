from tkinter import *

root = Tk()
# basket to store your data
basket = []

def add(option):
    basket.append(option)

def show_basket():
    print(basket)

b1 = Button(root, text='Netflix', command=lambda:  add('Netflix'))
b1.pack()
b2 = Button(root, text='Amazon',command=lambda: add('Amazon'))
b2.pack()
b3 = Button(root, text='Discovery', command=lambda: add('Discovery'))
b3.pack()
b4 = Button(root, text='Show Basket', command=show_basket)
b4.pack()

root.mainloop()


# ======================2nd example =================================
from tkinter import *

root = Tk()
# basket to store your data
basket = []


def add(option):
    basket.append(option)
    l = Label(root, text = option)
    l.pack()


b1 = Button(root, text='Netflix', command=lambda: add('Netflix'))
b1.pack()
b2 = Button(root, text='Amazon',command=lambda: add('Amazon'))
b2.pack()
b3 = Button(root, text='Discovery', command=lambda: add('Discovery'))
b3.pack()

root.mainloop()


