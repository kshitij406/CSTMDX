from tkinter import *

root = Tk()
root.geometry('300x300')
names = []
prices = []

count_items = IntVar()

def add(item):
    names.append(item[0])
    prices.append(item[1])
    count_items.set(count_items.get()+1)

counter_label = Label(root, textvariable=count_items, background='yellow')
counter_label.place(x=220, y=10)

amazon_item = ['Amazon', 200]
amazon_label = Label(root, text='Amazon')
amazon_label.place(x=10, y=25)
amazon_button = Button(root, text = 'ADD',command=lambda: add(amazon_item))
amazon_button.place(x=110, y=25)

apple_item = ['Apple', 100]
apple_label = Label(root, text='Apple')
apple_label.place(x=10, y = 70)
apple_button = Button(root, text = 'ADD',command=lambda: add(apple_item))
apple_button.place(x=110, y=70)


root.mainloop()