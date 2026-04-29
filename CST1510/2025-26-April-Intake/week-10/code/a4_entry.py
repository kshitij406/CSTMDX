from tkinter import *

root = Tk()
root.title('Entry ')
root.geometry("700x100+100+100")

# functionality on button
def button_func():
    if password.get() == '1234':
        print('Welcome ')
    else:
        print('Incorrect password')

# string object variable to get and set the value from and to the entry widget
password = StringVar()

# creating widgets
label = Label(root, text="Enter your password:")
entry = Entry(root, textvariable= password ) # you can add show='*' to hide the text
button = Button(root, text="Enter", bg='light gray', relief=RAISED, command=button_func)

# attaching widgets
label.pack(side=LEFT, padx=40, pady=10)
entry.pack(side=LEFT, padx=20, pady=10)
button.pack(side=LEFT, padx=40, pady=10)

root.mainloop()



