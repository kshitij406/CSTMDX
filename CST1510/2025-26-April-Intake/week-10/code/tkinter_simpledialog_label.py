
from tkinter import *
from tkinter import simpledialog

root = Tk()

answer = simpledialog.askstring("Input", "What is your first name?",
                                parent=root)
name_text = ''
if answer is not None:
    name_text = "Your first name is "+ answer
else:
    name_text = "You don't have a first name?"

name_label = Label(root, text=name_text)
name_label.pack()



answer = simpledialog.askinteger("Input", "What is your age?",
                                 parent=root,
                                 minvalue=0, maxvalue=100)
age_text = ''
if answer is not None:
    age_text = "Your age is "+ str(answer)
else:
    age_text = "You don't have an age?"

name_label = Label(root, text=age_text)
name_label.pack()

answer = simpledialog.askfloat("Input", "What is your salary?",
                               parent=root,
                               minvalue=0.0, maxvalue=100000.0)
salary_text = ''
if answer is not None:
    salary_text = "Your salary is "+ str(answer)
else:
    salary_text = "You don't have a salary?"

name_label = Label(root, text=salary_text)
name_label.pack()

root.mainloop()