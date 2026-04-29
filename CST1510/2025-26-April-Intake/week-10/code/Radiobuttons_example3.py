from tkinter import *


def retrieve():
    print(Var1.get())

root = Tk()
root.geometry("200x150")
frame = Frame(root)
frame.pack()

Var1 = IntVar()

RBttn = Radiobutton(frame, text="Burger", variable=Var1,
                    value=1, command=retrieve)
RBttn.pack(padx=5, pady=5)

RBttn2 = Radiobutton(frame, text="Pizza", variable=Var1,
                     value=2, command=retrieve)
RBttn2.pack(padx=5, pady=5)

root.mainloop()