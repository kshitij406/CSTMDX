'''https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/cursors.html'''
from tkinter import *


root = Tk()
root.title('cursors')
root.geometry("300x200+350+250")
root.bell()


label = Label(root, text="Welcome", bg='OldLace', cursor='star',fg='MistyRose4')
label.pack(side=TOP, padx=40, pady=10)

label_frame = LabelFrame(root, width=300, height=140, cursor='rtl_logo', background='OldLace', bd=3, relief=RAISED)
label_frame.pack()

root.mainloop()