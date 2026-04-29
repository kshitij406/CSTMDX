
from tkinter import *
from tkinter import simpledialog

root = Tk()



answer = simpledialog.askstring("Input", "What is your first name?",parent=root)


if answer is not None:
    print("Your first name is ", answer)
else:
    print("You don't have a first name?")

answer = simpledialog.askinteger("Input", "What is your age?",
                                 parent=root,
                                 minvalue=0, maxvalue=10)
if answer is not None:
    print("Your age is ", answer)
else:
    print("You don't have an age?")

answer = simpledialog.askfloat("Input", "What is your salary?",
                               parent=root,
                               minvalue=0.0, maxvalue=100000.0)
if answer is not None:
    print("Your salary is ", answer)
else:
    print("You don't have a salary?")

root.mainloop()