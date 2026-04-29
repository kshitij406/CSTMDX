from tkinter import *

root = Tk()

text_space = Text(root)
text_space.pack(pady=10, padx=10)

text_space.config(background = 'light gray', state=NORMAL, bd=2, relief=RAISED)
text_space.insert("end", 'hello world')
# text_space.see("end")
text_space.config(state=DISABLED)



root.mainloop()

