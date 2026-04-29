from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Label')
root.geometry("300x200+350+250")

label = Label(root, text="Welcome", bg='gray75')
label.pack(side=TOP, padx=40, pady=10)


root.mainloop()