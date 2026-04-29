from tkinter import *

root = Tk()

def hover_enter(event):
    l2.config(text='I want this text to show!')

def hover_exit(event):
    l2.config(text='')

l1 = Label(root, text='Hover over me!', width=20, height=1)
l1.pack(pady=20, padx=20)
l1.bind('<Enter>', hover_enter)
l1.bind('<Leave>', hover_exit)

l2 = Label(root, text = '', width=20, height=1, background='light gray')
l2.pack(pady=20, padx=20)


root.mainloop()

