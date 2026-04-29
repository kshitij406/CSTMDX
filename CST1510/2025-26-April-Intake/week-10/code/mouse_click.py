from tkinter import *

root = Tk()

def leftclick(event):
    print("left")

def middleclick(event):
    print("middle")

def rightclick(event):
    print("right")

frame = Frame(root, width=300, height=250)

frame.bind_all("<Button-1>", leftclick)

frame.bind("<Button-2>",rightclick )

frame.bind("<Button-3>",middleclick )

# oh177

frame.pack()
root.mainloop()