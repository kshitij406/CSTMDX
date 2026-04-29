
from tkinter import *



root = Tk()
root.geometry("500x50+350+250")

# Creating a tuple containing
# the specifications of the font.
font_comic = ("Comic Sans MS", 20, "bold")


l1 = Label(root, text="FLAT", border=5, relief=FLAT,fg='dark orange', bg='light green', font = font_comic)
l1.pack(side=LEFT,ipadx=10, ipady=10)
l2 = Label(root, text="RAISED", border=5, relief=RAISED,fg='black', bg='light salmon', font = font_comic)
l2.pack(side=LEFT, ipadx=10, ipady=10)
l3 = Label(root, text="SUNKEN", border=5, relief=SUNKEN, fg='dark sea green', bg='light sky blue', font = font_comic)
l3.pack(side=LEFT,ipadx=10, ipady=10)
l4 = Label(root, text="GROOVE", border=5, relief=GROOVE, fg='dark slate gray', bg='light slate gray', font = font_comic)
l4.pack(side=LEFT,ipadx=10, ipady=10)
l5 = Label(root, text="RIDGE", border=5, relief=RIDGE, fg='LightGreen', bg='light yellow',  font = font_comic)
l5.pack(side=LEFT, ipadx=10, ipady=10)

root.mainloop()