# importing everything from tkinter
from tkinter import *

# create gui window
root = Tk()

# set the configuration
# of the window
root.geometry("220x100")


# define a function
# for setting the new text
def java():
    my_string_var.set("You must go with Java")


# define a function
# for setting the new text
def python():
    my_string_var.set("You must go with Python")


# create a Button widget and attached
# with java function
btn_1 = Button(root,
               text="I love Android",
               command=java)

# create a Button widget and attached
# with python function
btn_2 = Button(root,
               text="I love Machine Learning",
               command=python)

# create a StringVar class
my_string_var = StringVar()

# set the text
my_string_var.set("What should I learn")

# create a label widget
my_label = Label(root, textvariable=my_string_var)

# place widgets into
# the gui window
btn_1.pack()
btn_2.pack()
my_label.pack()

# Start the GUI
root.mainloop()