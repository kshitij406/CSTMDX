from tkinter import *

root = Tk()
root.title('Relief styles')
root.geometry("500x50+350+250")

l1 = Label(root, text="FLAT", border=5, relief=FLAT, bg='aquamarine', fg='azure')
l1.pack(side=LEFT,ipadx=10, ipady=10)
l2 = Label(root, text="RAISED", border=5, relief=RAISED, bg='aquamarine', fg='azure')
l2.pack(side=LEFT, ipadx=10, ipady=10)
l3 = Label(root, text="SUNKEN", border=5, relief=SUNKEN, bg='bisque4', fg='black')
l3.pack(side=LEFT,ipadx=10, ipady=10)
l4 = Label(root, text="GROOVE", border=5, relief=GROOVE, bg='aquamarine', fg='azure')
l4.pack(side=LEFT,ipadx=10, ipady=10)
l5 = Label(root, text="RIDGE", border=5, relief=RIDGE, bg='blue violet', fg='azure')
l5.pack(side=LEFT, ipadx=10, ipady=10)

root.mainloop()

