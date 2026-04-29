from tkinter import *
from tkinter import simpledialog

root = Tk()
root.title('Label')
root.geometry("300x200+350+250")

# ====================Name Entry ===================================
# create a StringVar class
my_string_var = StringVar()

# setting font
comic_font = ("Comic Sans MS", 20, "bold")

# window asking for the username
answer = simpledialog.askstring("Input", "What is your first name?",parent=root)
if answer is not None:
    # set value to string variable
    my_string_var.set(f"Welcome {answer} 😄 ")

label = Label(root, textvariable=my_string_var, bg='gray75', bd=5, relief=RAISED, font=comic_font)
label.pack(side=TOP, padx=40, pady=10)

# get value from string variable
label_frame = LabelFrame(root, width=300, height=140, text=my_string_var.get())
label_frame.pack()

root.mainloop()